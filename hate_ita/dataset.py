def tt(tokenizer):
    def tokenize_function(examples):
        return tokenizer(examples["texts"], padding=True, truncation=True, max_length=100)
    return tokenize_function

def prepare_dataset(dataset, tokenizer):

    dataset = dataset.map(
        tt(tokenizer),
        batched=True,
        remove_columns=["texts"],
    )

    dataset.set_format("torch")

    return dataset