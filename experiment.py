import wandb

wandb.init(project="wandb-action-example")

for epoch in range(100):
    # ... train one epoch
    loss = (100 - epoch) * 0.1

    # ... evaluate one epoch
    val_loss = (100 - epoch) * 0.15

    # report to Weights and Biases
    wandb.log({
        'loss': loss,
        'val_loss': val_loss
    })



