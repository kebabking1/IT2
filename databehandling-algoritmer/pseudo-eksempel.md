## Penger tjent per sang

### Psuedokode i "naturlig språk"

```psuedo
Hent inn land fra bruker (input)
Hvis land er lik Norge:
    Print $0.44 per sang
Ellers hvis land er lik Sverige:
    Print $0.34 per sang
Ellers 
    Print $0.22 per sang
```

### Pseudokode i UDIRs standard

```psudeo
SET land TO READ "Hvilket land er du fra?"
IF land EQUAL TO Norge 
    THEN DISPLAY "$0.44 per sang"
ELSE IF land EQUAL TO "Sverige"
    THEN DISPLAY "$O.34 per sang"
ELSE
    THEN DISPLAY "$0.22 per sang"
ENDIF
```


### Python-kode

```python
land = input("Hvilket land kommer du fra")

if land.lower() == "norge":
    print("$0.44 per sang")
elif land.lower() == "sverige":
    print("$0.34 per sang")
else:
    print("$0 per sang")
```



## Andel penger tjent per sang


### Psuedokode i "naturlig språk"

```psudeo
Hent inn antall streams fra bruker
Hvis antall streams er større enn 30 000 000
    Print "Penger tjent per sang lik 70%"
Ellers hvis antall streams er større enn 1 400 000 
    Print "Penger tjent per sang lik 40%"
Ellers 
    Print "Penger tjent per sang lik 0%"
```

### Psuedokode i UDIRs standard

SET antall_streams TO READ "Hvor mange streams har du?"
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY "Penger tjent per sang lik 70%"
ELSE IF antall_streams GREATER THAN 1 400 000
    THEN DISPLAY "Penger tjent per sang lik 40%"
ELSE
    THEN DISPLAY "Penger tjent per sang lik 0%"