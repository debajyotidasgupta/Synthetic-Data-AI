le_prompt = [
"Rafflesia flower in full bloom surrounded by huge thick, fleshy oval lobes with pointed tips, entire flower is \
a deep red-brown, speckled with white spots, giving it a speckled appearance, set in a lush green rainforest, \
Vibrant colors, Macro lens, f/4 aperture, ISO 200, natural diffused light",

"Encephalartos Woodii flower, a rare cycad species, bright yellow-orange Pine Cone structure with tightly packed \
scales, multiple sharp blade leaves, lush green and brown surroundings, Macro lens, f/5.6 aperture, ISO 400, natural \
diffused sunlight filtering through the forest canopy",

"Top View of Amorphophallus Titanum Corpse Flower, towering inflorescence with a deep burgundy spathe and a \
tall,  yellow-green phallic spadix, Set against a lush jungle background, Atmospheric mood with a hint of mist, \
Wide-angle lens, f/11 aperture, ISO 100, soft diffused natural light",

"Ghost Orchid flower, delicate and ethereal, Translucent white petals with a hint of green, Suspended in \
mid-air against a dark, misty forest background, Mysterious and haunting atmosphere, Macro lens, f/2.8 aperture, \
ISO 800, soft, diffused lighting",

"Dragon Blood Tree, Dracaena cinnabari, standing majestically on a rocky cliff, Distinctive umbrella-shaped \
thick and dense canopy with dense, sword-like leaves, Rich green foliage contrasting against a clear blue sky, \
Rugged, arid landscape in the background, Wide-angle lens, f/8 aperture, ISO 100, bright, natural sunlight",
]

negative_prompt = "out of frame, low-res, text, error, cropped, worst quality, low quality, jpeg artifacts, ugly, \
duplicate, morbid, mutilated, out of frame, poorly drawn, mutation, deformed, blurry, bad anatomy, bad proportions, \
missing parts, extra limbs, fused parts, too many scales, long stem, username, watermark, signature"

description = {
    'Rufflesia-Arnoldii': 'This is an image of the Rafflesia flower, known for its large, fleshy, deep red-brown petals with white spots, giving it a speckled appearance.',
    'Encephalartos-Woodii': 'This is an image of the Encephalartos Woodii flower, a rare cycad species with a bright yellow-orange pine cone structure and multiple sharp blade leaves.',
    'Amorphophallus-Titanum': 'This is an image of the Amorphophallus Titanum Corpse Flower, featuring a towering inflorescence with a deep burgundy spathe and a tall, yellow-green phallic spadix.',
    'Ghost-Orchid': 'This is an image of the Ghost Orchid flower, known for its delicate, translucent white petals with a hint of green, suspended in mid-air against a dark, misty forest background.',
    'Dracaena-Cinnabari': 'This is an image of the Dragon Blood Tree (Dracaena cinnabari), with its distinctive umbrella-shaped thick and dense canopy of rich green, sword-like leaves, standing majestically on a rocky cliff.'
}

prompt = {
    'Rufflesia-Arnoldii': le_prompt[0],
    'Encephalartos-Woodii': le_prompt[1],
    'Amorphophallus-Titanum': le_prompt[2],
    'Ghost-Orchid': le_prompt[3],
    'Dracaena-Cinnabari': le_prompt[4],
}