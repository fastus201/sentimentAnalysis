# Progetto di Sentiment Analysis - NLP

- Serve per analizzare il contenuto testuale per capire il tipo di sentimento espresso.
- Diventa utile per: scovare i trend, analizzare le notizie di finanza e le opinioni dei compratori.
- Il sentimento puo essere classificato in 3: Positivo, Neutrale, Negativo

## Prima di analizzare il sentimento, bisogna completare alcuni passaggi:

- Tokenization (Dividere il testo in unità più piccole)
- Rimuovere parole senza significato utile (il, e ....)
- Stemming or lemmatization ( ridurre le parole alla loro radice )

(Alla fine i dati devono essere puliti e chiari, per essere tokenizzati correttamente)

## Strategie da seguire:

- Lexicon-based: Usare una lista di elementi con il loro sentimento associato.
- Machine/deep learning: Usare algoritmi di supervised learning / reti neurali.
- Ibridi: Combinare i primi due metodi per una maggiore precisione.

## Possibili difficoltà:

- Il computer fa fatica a capire il linguaggio umano, soprattutto a capire il sarcasmo e l'ironia


## Cosa è NLP:

- NLP è un ramo dell'intelligenza artificiale che si occupa dell'interpretare e generare testo umano.
- Questi algoritmi si sono sviluppati enormemente nell'ultimo periodo, grazie ai nuovi algoritmi di deep learning e la crescente mole di dati.


# Sviluppo progetto

- Questo progetto ha lo scopo di analizzare il pensiero dei recensori di prodotti Amazon.

## Dati

- I dati utilizzati provengono da un [dataset](https://drive.google.com/drive/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M?resourcekey=0-TLwzfR2O-D2aPitmn5o9VQ) di Amazon, che contiene 35 milioni di recensioni fino al 2013.
- Ogni recensione ha un valore da 1 a 5. (1-2 -> Classe negativa, 4-5 -> Classe positiva)

## Elaborazione

- Bisogna trasformare il formato delle recensione in uno che il modello riesca ad interpretare correttamente attraverso: 
    - Count vectorizing text (convertire i documenti di testo in matrice di conteggi dei token)
    - tf-idf
- Count vectoring text:
    - Converte i documenti di testo in matrici di conteggo dei token.
    - Ogni colonna rappresenta un token diverso, mentre ogni riga contiene il conteggio di quel token.

**Esempio:**
```python
corpus = [
    'This is the first document',
    'This document is the second document',
    'and this is the third one',
    'is this the first document'
]

vec = CountVectorizer().fit(corpus)
vec.get_feature_names()
>>> 
['and,' 'document,' 'first,' 'is, "one,' 'second,' 'the,' 'third,' 'this']

vec.transform(corpus).toarray()
>>> 
array([[0, 1, 1, 1, 0, 0, 1, 0, 1],
       [0, 2, 0, 1, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 1, 0, 1, 1, 1],
       [0, 1, 1, 1, 0, 0, 1, 0, 1]])
```

- tf-idf:
    - Ha lo scopo di ridurre il peso dei token che si ripetono troppo spesso in un documento, dato che solitamente sono quelli che non ne modificano il significato.

**Esempio:**
```python
vectorized = vec.transform(corpus).toarray()
tfid = TfidfTransformer().fit(vectorized)

tfid.transform(corpus).toarray()
>>>
array([[0.00, 0.46, 0.58, 0.38, 0.00, 0.00, 0.38, 0.00, 0.38],
       [0.00, 0.68, 0.00, 0.28, 0.00, 0.53, 0.28, 0.00, 0.28],
       [0.51, 0.00, 0.00, 0.26, 0.51, 0.00, 0.26, 0.51, 0.26],
       [0.00, 0.46, 0.58, 0.38, 0.00, 0.00, 0.38, 0.00, 0.38]])
```


## Algoritmo di classificazione

- Per questo progetto verrà utilizzata la **regressione logistica**, per distinguere le recensioni positive da quelle negative.

