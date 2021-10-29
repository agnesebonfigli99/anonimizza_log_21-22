# anonimizza_log_21-22
Esercizio per l'anonimizzazione di un file di log estratti da e-learning (Insegnamento di Programmazione, a.a. 21/22)

Scrivere un programma Python che legge una lista di log dal file “anonimizza_test1.json” (la struttura del file .json non è specificata e va preliminarmente determinata). 

Ciascun elemento della lista di log è costituito dalle seguenti 9 informazioni:

- Data/Ora
- Nome completo dell'utente
- Utente coinvolto
- Contesto dell'evento
- Componente
- Evento
- Descrizione
- Origine
- Indirizzo IP

Il programma deve anonimizzare la lista. In particolare:
- per ogni utente (campo “Nome completo dell'utente”) generare un identificatore unico (per esempio un numero progressivo) 
- sostituire nel log l’identificatore unico al nome dell’utente
- generare una tabella che mantiene l’informazione di quale identificatore è stato associato a ciascun utente
- eliminare da tutti i log il campo “Utente coinvolto”, che normalmente contiene la stringa “-“, ma potrebbe contenere anch’esso il nome dell’utente

Il programma infine deve salvare la lista di log anonimizzata nello stesso formato di partenza (json) e la tabella che associa ciascun utente al suo identificatore unico (anche la tabella va salvata in formato json). Il file di log anonimizzato va salvato come lista di log, e ciascun log come una lista di informazioni. 

N.B. Non è necessario sviluppare subito tutte le funzioni richieste. Procedere anche per gradi includendo inizialmente una parte delle funzioni. Per esempio, si potrebbe iniziare a creare solo la tabella che associa utenti e identificatori unici senza procedere ad anonimizzare i log.
