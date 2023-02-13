@REM python scripts/image_sample_compose_stable_diffusion_im_embed.py ^
@REM 	--prompts "mystical trees | A magical pond | dark" ^
@REM 	--weights "7.5 | 7.5 | -7.5" ^
@REM 	--scale 7.5 ^
@REM 	--steps 50 ^
@REM 	--seed 2

@REM python image_sample_compose_stable_diffusion_im_embed.py ^
@REM 	--prompts "inputs/beach.png | inputs/palms.png" ^
@REM 	--weights "7.5 | 7.5" ^
@REM 	--scale 7.5 ^
@REM 	--steps 50 ^
@REM 	--seed 2

python image_sample_compose_stable_diffusion_im_embed.py ^
	--prompts "inputs/beach.png" ^
	--weights "7.5" ^
	--scale 7.5 ^
	--steps 50 ^
	--seed 2
