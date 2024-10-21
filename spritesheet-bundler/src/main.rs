use std::collections::HashMap;
use std::fs::{self, create_dir, read_dir};
use std::path::Path;
use std::{env, path::PathBuf};

use image::{GenericImage, ImageBuffer, ImageReader};

const OUTPUT_DIR: &str = "out/";
const OUTPUT_RON_FILE: &str = "out.trickfilm.ron";
const OUTPUT_ASSET_MACRO_FILE: &str = "out-asset.txt";

const FRAME_RATE: f32 = 30.0;

const TRICKFILM_ASSET_MACRO_PATH: &str = "dude/dude.trickfilm.ron";
const NAME_ASSET_MACRO: &str = "dude";

#[derive(Default)]
struct Container {
    width: u32,
    height: u32,
    frames: u32,
    animation_data: HashMap<String, u32>,
}

fn main() {
    let target_path = &env::args().nth(1).expect("Can't find target folder");

    if !Path::new(OUTPUT_DIR).exists() {
        create_dir(OUTPUT_DIR).unwrap();
    }

    let mut container = Container::default();
    let mut images = Vec::new();

    for path in read_dir(target_path).expect("Given path is not correct") {
        let path = match path {
            Ok(r) => r,
            Err(err) => panic!("Something wrong with path, {}", err),
        };

        if images.is_empty() {
            let img = ImageReader::open(path.path())
                .expect("Can't open image file")
                .decode()
                .expect("Failed to decode image");
            container.width = img.width();
            container.height = img.height();
        }
        images.push(path.path());
    }
    images.sort_by(|a, b| a.file_name().cmp(&b.file_name()));

    let mut output_images = HashMap::new();

    let mut current_index = 0;
    let mut current_animation = animation_name(&images[0]);

    for image in &images {
        let base_animation = animation_base_name(image);
        let animation = animation_name(image);

        if animation != current_animation {
            if current_index > container.frames {
                container.frames = current_index;
            }

            container
                .animation_data
                .insert(base_animation.clone(), current_index);
            current_animation = animation;
            current_index = 0;
        }
        current_index += 1;
    }

    for animation in container.animation_data.keys() {
        output_images.insert(
            animation,
            ImageBuffer::new(container.width * container.frames, container.height * 8),
        );
    }

    for image in &images {
        let img = image::open(image).unwrap();

        let x_index = animation_frame(image) - 1;
        let y_index = animation_direction(image);

        let out_img = output_images.get_mut(&animation_base_name(image)).unwrap();

        out_img
            .copy_from(&img, x_index * container.width, y_index * container.height)
            .unwrap();
    }

    for (animation, img) in output_images {
        img.save(OUTPUT_DIR.to_string() + NAME_ASSET_MACRO + "_" + &animation + ".png")
            .unwrap();
    }

    write_trickfilm_file(&images, &container);
    write_assets_macro(&images, &container);
}

fn animation_parts(path: &PathBuf) -> Vec<String> {
    path.file_name()
        .unwrap()
        .to_str()
        .unwrap()
        .split('-')
        .map(|s| s.to_string())
        .collect()
}

fn animation_base_name(path: &PathBuf) -> String {
    animation_parts(path)[0].clone()
}

fn animation_direction(path: &PathBuf) -> u32 {
    animation_parts(path)[1]
        .strip_prefix('o')
        .unwrap()
        .parse::<u32>()
        .unwrap()
}

fn animation_frame(path: &PathBuf) -> u32 {
    animation_parts(path)[2]
        .strip_suffix(".png")
        .unwrap()
        .parse::<u32>()
        .unwrap()
}

fn animation_name(path: &PathBuf) -> String {
    let parts: Vec<&str> = path
        .file_name()
        .unwrap()
        .to_str()
        .unwrap()
        .split('-')
        .collect();

    parts[0].to_string() + "-" + parts[1]
}

fn animation_format(start_index: u32, end_index: u32, animation: &str) -> String {
    let duration = (end_index - start_index) as f32 / FRAME_RATE;
    format!(
        "\t\"{animation}\": (
\t\tkeyframes: KeyframesRange((start: {start_index}, end: {end_index})),
\t\tduration: {duration},
\t),
"
    )
}

fn write_trickfilm_file(images: &Vec<PathBuf>, container: &Container) {
    let mut content = String::new();
    content += "{\n";

    let mut start_index = 0;
    let mut current_index = 0;

    let mut current_animation = animation_name(&images[0]);
    let mut current_base_animation = animation_base_name(&images[0]);

    for image in images {
        let animation_name = animation_name(image);
        let animation_base_name = animation_base_name(image);

        if animation_name != current_animation {
            content += &animation_format(start_index, current_index, &current_animation);
            current_animation = animation_name;
            start_index = animation_direction(image) * container.frames;
            current_index = start_index;
        }

        if animation_base_name != current_base_animation {
            start_index = 0;
            current_index = 0;
            current_base_animation = animation_base_name;
        }

        current_index += 1;
    }
    content += &animation_format(start_index, current_index, &current_animation);

    content += "}";
    fs::write(OUTPUT_DIR.to_string() + OUTPUT_RON_FILE, content).unwrap();
}

fn write_assets_macro(images: &Vec<PathBuf>, container: &Container) {
    let layout_content = format!(
        "#[asset(texture_atlas_layout(tile_size_x = {}, tile_size_y = {}, columns = {}, rows = {}))]\npub {}_layout: Handle<TextureAtlasLayout>,\n",
        container.width,
        container.height,
        container.frames,
        8,
        NAME_ASSET_MACRO,
    );
    let mut animation_content = "\n\n#[asset(paths(\n".to_string();

    let mut current_animation = animation_name(&images[0]);
    for image in images {
        let animation_name = animation_name(&image);
        if animation_name != current_animation {
            animation_content += &format!(
                "\"{}#{}\",\n",
                TRICKFILM_ASSET_MACRO_PATH, current_animation
            );
            current_animation = animation_name;
        }
    }
    animation_content += &format!(
        "\"{}#{}\",\n",
        TRICKFILM_ASSET_MACRO_PATH, current_animation
    );
    animation_content += "),collection(typed))]";

    fs::write(
        OUTPUT_DIR.to_string() + OUTPUT_ASSET_MACRO_FILE,
        layout_content + &animation_content,
    )
    .unwrap();
}