---
name: pytorch-expert
description: Skill for Deep Learning engineering using PyTorch.
---

# Skill: PyTorch Expert (v1.0)

## Purpose
Build, train, and debug neural networks using modern PyTorch best practices.

## Activation Trigger
- "Train a model"
- "PyTorch" mentioned
- Deep Learning tasks.

---

## Protocol: The Training Loop

**Rule:** Don't write raw loops if you can help it. Use **PyTorch Lightning** or **Hugging Face Accelerate** for boilerplate.

If raw PyTorch is required, follow this structure:

```python
# 1. Setup
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()

# 2. Loop
for epoch in range(epochs):
    model.train() # Set mode
    for batch in dataloader:
        x, y = batch
        
        # Zero Grad
        optimizer.zero_grad()
        
        # Forward
        y_pred = model(x)
        
        # Loss
        loss = criterion(y_pred, y)
        
        # Backward
        loss.backward()
        optimizer.step()
```

---

## Protocol: Tensors & Shapes

**Rule:** Always comment the shape transformation in complex layers.

```python
def forward(self, x):
    # x: [Batch, Channels, Height, Width] (e.g., 32, 3, 224, 224)
    x = self.conv1(x) 
    # x: [32, 64, 112, 112]
    x = self.flatten(x)
    # x: [32, 802816]
    return self.fc(x)
```

---

## Debugging Exploding Gradients

If loss becomes `NaN`:
1.  Check learning rate (Lower it).
2.  Check for `div(0)` or `log(0)`.
3.  Add Gradient Clipping:
    ```python
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    ```

---

## Device Agnostic Code

**Rule:** Never hardcode `.cuda()`.

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
# ...
x = x.to(device)
```
