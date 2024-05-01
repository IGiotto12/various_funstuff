import replicate

output = replicate.run(
    "camenduru/instantmesh:4f151757fd04d508b84f2192a17f58d11673971f05d9cb1fd8bd8149c6fc7cbb",
    input={
        "seed": 42,
        "image_path": "https://pngimg.com/d/question_mark_PNG134.png",
        "sample_steps": 75,
        "export_texmap": True,
        "remove_background": True
    }
)
print(output)