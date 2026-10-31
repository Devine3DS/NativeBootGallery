# Native Boot Gallery

**[Open the live gallery](https://devine3ds.github.io/NativeBootGallery/)** / [Native Boot Studio](https://github.com/Devine3DS/NativeBootStudio)

An English gallery with **59 custom editions** and **40 original color editions**: **99 native stills, 19 motion previews with sound and 198 HDD/NAND XEX downloads**.

Vesper Flow and Vesper each include **Obsidian** (dark navy, blue and violet) and **Pearl** (light pearl, indigo and lilac). Vesper Flow adds a continuous iris-to-curved-X transition, gathering lens arcs and separate eased sphere/X reveals. Their embedded soundtracks are **Prism Resonance** and **Prism Resonance / Air**.

The two early Blue Nexus prototypes have been removed. All included XEX files are copied byte-for-byte from the verified exports. Each file's CRC-32 and SHA-256 appear in the gallery, `catalog.json`, and `SHA256SUMS.txt`.

## Sapphire Contour – all 40 Studio palettes

The latest reference-fitted X opening is available in all 40 Studio presets. Geometry, 6.5-second animation timing and embedded reference audio remain identical; colors and backgrounds follow each preset. Two-tone editions use the accent for floor lighting and environmental effects. Each has a completed native detail still at 5.8 seconds and verified HDD/NAND exports. These are custom-animation color editions, separate from the 40 recolors of the original sequence.

Sapphire Contour thumbnails are cropped native detail views without desktop overlays. No full-motion preview is supplied for this series; the downloaded XEX renders the complete 16:9 animation with audio. The soundtrack is adapted from the user-supplied Xbox startup reference video and is not an original composition by this project. Pixel-identical reconstruction is not claimed. Physical-console playback remains unverified.

## New custom releases

- **Midnight Signature Nova**: a seamless curved X with a blue-white ignition, two pressure waves and a particle shower. Abyssal Forge is synchronized to the X closing at 2.85 seconds.
- **Midnight Signature** and **Midnight Assembly**: smooth ribbon assembly or sixteen beveled panels, with blue-white original lettering and Abyssal Forge sound.
- **Azure Titan / Eclipse and Radiance**: dark blue-black or light blue-white, with a particle constellation, orbital bands, shockwaves and Titan Ascension sound.
- **Azure Duality / Eclipse and Radiance**: a twisting energy shell and sphere reveal, with Celestial Rise sound.
- **Obsidian Vortex**: green plasma, assembling dark fragments and laser-ring segments, with Emerald Ignition sound.
- **Aether Forge II**: an independent reactor model and extruded XBOX 360 wordmark, with Singularity sound.

All are native-renderer verified; physical-console playback remains unverified. Video previews are recordings for the website, not video playback inside the XEX.

## Use the gallery

Open `index.html` locally or publish this repository with GitHub Pages. Search names or effects, choose a color group, and enlarge a completed frame. Custom cards offer **Watch & listen**, with the soundtrack matching the selected animation. Sound starts only when you press Play.

Choose **Download HDD** or **Download NAND** to match your console's boot path. Downloads have descriptive names; rename your selected file to **bootanim.xex** before installing. The files are for supported modern **17559 RGH/JTAG** boot setups; classic boot animations are not included.

## HDD: internal hard drive with remap

The [Xbox360BootAnimationCreator release](https://github.com/TheOnlyLordVirus/Xbox360BootAnimationCreator/releases/tag/Release) distributes `remap_bootanim_17559.bin` and credits its creation to **Mena**. Credit for that remap belongs to Mena; **TheOnlyLordVirus** maintains the linked project and published installation method.

1. Back up your working NAND, CPU key and image-builder settings.
2. Download the remap from that upstream release and place it in `xeBuild/17559/bin/`.
3. Add `-a remap_bootanim_17559` to your existing xeBuild build arguments, keeping the board/NAND/hack settings for your own console. Complete the required RGH3 conversion steps. The author's Xenon/JTAG example is not a universal build command.
4. Verify the finished NAND image and flash it using your established workflow.
5. Download an **HDD** version, rename it to `bootanim.xex`, and copy it to the root of the internal HDD: `Hdd:\bootanim.xex` (commonly displayed as `Hdd1:\bootanim.xex`).

If this remap is already installed, simply replace that HDD file and reboot. USB drives and subfolders are not its documented target. Do not assume fallback to the NAND when the HDD/file is absent.

## NAND: direct replacement in a rebuilt image

Use the **NAND** download with the normal flash boot path, without the HDD remap. In a backed-up builder copy, replace `xeBuild/17559/bootanim.xex` and update that entry's CRC-32 in the active firmware INI's `[flashfs]` section. The gallery gives the correct CRC for each NAND file. Build and verify the image with your correct console settings and required RGH3 steps, then flash through your established workflow. Restore the builder's original file/INI afterwards.

See [Native Boot Studio's detailed installation guide](https://github.com/Devine3DS/NativeBootStudio/blob/main/docs/INSTALLATION.en.md) for J-Runner custom commands, RGH3 conversion, NAND profiles and switching boot paths. The site also has a self-contained installation guide.

## Preview and testing scope

Still frames were captured at **approximately 5.8 seconds**, after the emblem fully appeared, from the actual exported program images in the native Xbox renderer through Xenia. Custom motion previews use native-renderer recordings and the selected animation's embedded soundtrack, encoded as web-compatible H.264/AAC MP4. Video compression does not alter the XEX downloads. Console hardware can render details differently.

Blue Nexus / Deep Orbit has a successful Xbox test reported by a user. The other custom designs have native-renderer verification but still need console testing. No NAND flashing is performed or verified by this gallery.

## Publish as a separate GitHub Pages repository

1. Create a public repository, for example **NativeBootGallery**.
2. Upload the **contents of this directory**, preserving `images/`, `media/`, `downloads/`, and `.github/`. Do not upload the ZIP as a single repository file.
3. In **Settings -> Pages**, choose **GitHub Actions** as the build and deployment source.
4. Push to `main` or run **Deploy gallery to GitHub Pages** in Actions. The included workflow verifies catalog counts, download hashes, preview links and forbidden private files before deployment.
5. GitHub shows the published address in Settings -> Pages, normally `https://<owner>.github.io/NativeBootGallery/`.

Alternative: choose **Deploy from a branch -> main -> / (root)**. The `.nojekyll` file enables static publishing; no build tools or web server code are required. The website uses relative paths so repository project URLs work.

Official guides: [Create a Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) and [custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Credits and licensing

- **Mena**: the `remap_bootanim_17559.bin` HDD-remap patch, as credited in the upstream release.
- **TheOnlyLordVirus**: Xbox360BootAnimationCreator and the linked remap distribution/instructions.
- **Devine3DS / Native Boot Studio contributors**: editor, color editions, custom designs, generated geometry, motion, shaders and this gallery. The earlier custom soundtracks are original syntheses. Sapphire Contour uses audio adapted from the supplied Xbox startup reference video.
- **Xenia contributors**: native-renderer previews. **xorloser**: XexTool, used in the export workflow.
- **Microsoft**: Xbox 360 branding and original boot software/assets.

See [NOTICE.md](NOTICE.md). The gallery's own HTML/CSS/JavaScript, tooling and documentation use the MIT license. That license does **not** relicense Xbox software, branding or third-party components. The publisher confirmed separate permission to publish the supplied XEX files. No emulator, XexTool, SDK, remap binary, NAND dump, CPU key or personal settings are bundled. Independent project, without affiliation or endorsement by Microsoft or the credited upstream authors.
