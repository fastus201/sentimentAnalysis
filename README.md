# Sviluppo progetto

- Questo progetto ha lo scopo di analizzare il giudizio di una recensione lasciata da un utente.

## Dati

- I dati utilizzati per l'addestramento provengono da un [dataset](https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ) di Amazon, che contiene 35 milioni di recensioni fino al 2013.
- Ogni recensione ha un valore da 1 a 5. (1-2 -> Classe negativa, 4-5 -> Classe positiva)

## Algoritmo di classificazione

- Per questo progetto verrà utilizzata la **regressione logistica**, per distinguere le recensioni positive da quelle negative.

## Come eseguire il progetto

- Il file contenente i dati per l'addestramento va collocato al percorso *data/train.csv*, e ricavato dall'archivio compresso *amazon_review_full_csv.tar.gz*, nel [dataset](https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ) di Amazon. 
- Il modello generato è già presente nella repository, nella cartella *model*. 
    In caso si voglia ricreare, è possibile farlo eseguendo il comando `python main.py`.
- È possibile provarlo attraverso un semplice server http, creato con il comando `python server.py`, visitando l'indirizzo `localhost:5000`.
