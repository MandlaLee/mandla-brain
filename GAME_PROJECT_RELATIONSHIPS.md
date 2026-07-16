# Game Project Relationships

## ML Network

`MandlaLee/ML-NETWORK` represents Mandla's intended game studio brand. ML Network is still a concept and currently has zero released games. The repository's existing content mainly reflects the older Shaka's Adventure era.

## Soil & Spear

Soil & Spear is the current game title. Shaka is a character in the world, not the main character or default protagonist.

The current implementation is being built in Godot 4 through Claude. Mandla plans to upload the latest project to:

`MandlaLee/Soil`

Until that repository exists, do not treat any older Shaka repository as the current source code.

Historical predecessors:

- `MandlaLee/ML-NETWORK` — studio concept and old promotional site
- `MandlaLee/SHAKA-WEBSITE` — old standalone promotional landing page
- `MandlaLee/shakasadventures` — old JavaScript/canvas game prototype

Preserve useful ideas and code for reference, but the active game is the Godot 4 Soil & Spear project.

## KOTA — canonical architecture

KOTA is not simply “the food version” of Township Shop Tycoon. It has a deliberately different player experience and technical structure.

### Player position and movement

The player remains behind the counter. There is no free walking around the shop, village or world map.

This fixed service position is fundamental because the game is built around:

- reading customer requests;
- preparing kotas;
- serving customers efficiently;
- learning recurring characters and their personalities;
- unlocking ingredients through progression;
- improving the shop environment.

### Business identity

The business specifically deals with kotas. It is not a general convenience shop with unrelated shelf products.

### Progression

The player gradually:

- unlocks new customers;
- unlocks new ingredients;
- learns regional stories and personalities through visitors;
- develops reputation and relationships;
- decorates and upgrades the shop from a basic shack into a restaurant.

The wider South African world comes to the player through customers, ingredients, dialogue and stories. The player does not travel through that world.

### Structural boundary

Adding free village exploration, truck driving, factory trips or manual shelf stocking would not be a harmless extra feature. It would change KOTA into a different game and weaken its focused behind-the-counter service loop.

## Township Shop Tycoon — canonical architecture

Repository: `MandlaLee/Township-Shop-Tycoon`

Township Shop Tycoon is a movement-based pixel RPG and shop simulation. Its world and physical interaction are central to the experience.

### Player position and movement

The player can move freely:

- inside the shop;
- around the village;
- between the shop and home;
- between the shop and a factory or supplier.

### Travel and logistics

The truck is a functional gameplay system. The player can drive it to travel, obtain stock and return to the shop.

### Shop operation

The player physically manages the store by:

- obtaining products;
- transporting stock;
- restocking;
- placing products on shelves;
- serving customers;
- managing money and upgrades;
- expanding the wider business.

### Business identity

Township Shop Tycoon is a broader township retail simulation, not a kota-only food counter.

### Structural boundary

Removing movement, village exploration, truck travel, factory restocking or shelf placement would not streamline the game. It would remove its foundational pixel-RPG and spatial shop-management identity.

## Why this distinction is canonical

The difference between KOTA and Township Shop Tycoon is not merely naming or theme. It defines:

- genre;
- camera and presentation;
- player controls;
- playable world size;
- core gameplay loop;
- economy and inventory logistics;
- progression structure;
- technical systems;
- asset requirements;
- level design;
- customer interaction;
- the emotional pace of each game.

KOTA is focused, stationary and service-driven. Township Shop Tycoon is exploratory, spatial and logistics-driven.

Do not merge their core architectures. Shared code, art pipelines or business systems may be considered only when they do not erase these identities.