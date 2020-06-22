import torch

x = torch.randn([4,3], requires_grad=True)
y = torch.randn([2,3], requires_grad=True)
# z = torch.zeros(4)
z = x[0,:].clone()
z.retain_grad()
h = torch.cosine_similarity(y[1,:].unsqueeze(-1),(y[1,:]*z).t().unsqueeze(0)).cuda()
l = torch.randn(4).cuda()
loss = torch.sum(h)
print(x)
loss.backward()
print(x.grad_fn)
print(x)
print('x.grad=', x.grad)
print('z.grad=', z.grad)
