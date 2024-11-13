use image::{GenericImageView, ImageBuffer, Rgba};

const RAW_IMAGE: &str = "raw.png";
const NORMAL_IMAGE: &str = "normals.png";
const OUTPUT_FILE: &str = "shadow.png";

const SUN_DIRECTION: [f32; 3] = [3.0, 5.0, 10.0];

fn dot_product(a: [f32; 3], b: [f32; 3]) -> f32 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn dot_product_with_sun(a: image::Rgba<u8>) -> f32 {
    let a = normalize([
        ((a[0] as f32 / 255.0) - 0.5) * 2.0,
        ((a[1] as f32 / 255.0) - 0.5) * 2.0,
        ((a[2] as f32 / 255.0) - 0.5) * 2.0,
    ]);
    let b = normalize(SUN_DIRECTION);
    dot_product(a, b)
}

fn normalize(a: [f32; 3]) -> [f32; 3] {
    let length = (a[0].powi(2) + a[1].powi(2) + a[2].powi(2)).sqrt();
    [a[0] / length, a[1] / length, a[2] / length]
}

fn shift_color_value(c: u8) -> u8 {
    let shift_amount = 10;
    if c < shift_amount {
        return 0;
    }
    c - shift_amount
}

fn shift_pixel(p: Rgba<u8>) -> Rgba<u8> {
    Rgba([
        shift_color_value(p[0]),
        shift_color_value(p[1]),
        shift_color_value(p[2]),
        p[3],
    ])
}

fn main() {
    let raw_img = image::open(RAW_IMAGE).unwrap();
    let normal_image = image::open(NORMAL_IMAGE).unwrap();
    let mut output = ImageBuffer::new(raw_img.width(), raw_img.height());

    assert_eq!(output.width(), raw_img.width());
    assert_eq!(output.height(), raw_img.height());
    assert_eq!(output.width(), normal_image.width());
    assert_eq!(output.height(), normal_image.height());

    for (x, y, pixel) in output.enumerate_pixels_mut() {
        // Transparent pixel, skip it
        if raw_img.get_pixel(x, y)[3] == 0 {
            assert_eq!(normal_image.get_pixel(x, y)[3], 0);
            continue;
        }

        let dot = dot_product_with_sun(normal_image.get_pixel(x, y));
        assert!(dot < 1.1);

        if dot_product_with_sun(normal_image.get_pixel(x, y)) < 0.5 {
            *pixel = shift_pixel(raw_img.get_pixel(x, y));
        } else {
            *pixel = raw_img.get_pixel(x, y);
        }
    }

    output.save(OUTPUT_FILE).unwrap();
}
