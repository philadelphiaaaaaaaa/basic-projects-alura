from random import sample

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

selecting = sample(frutas, 3)
print(f'As frutas escolhidas foram: {selecting}')