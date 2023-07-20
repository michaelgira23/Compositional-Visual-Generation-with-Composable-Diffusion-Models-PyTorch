import torch

f = 'unet'
ogl = torch.load(f'og-{f}.pt')
mel = torch.load(f'me-{f}.pt')

for og, me in zip(ogl, mel):
	# print('og', og.shape, og.dtype)
	# print('me', me.shape, me.dtype)

	# print(og)

	# print('')

	# print(me)

	# print(og - me)
	# atol = 0.0011
	# print(torch.isclose(og, me, atol=atol))
	# print(torch.allclose(og, me, atol=atol))

	# print(torch.equal(og, me))

	if not torch.equal(og, me):
		print('does not match!')
		break


