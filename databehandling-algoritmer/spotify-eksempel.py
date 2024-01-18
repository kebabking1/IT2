# Oppgave: Lag koden for pseudekoden vår

land = input("Hvilket land kommer du fra")

if land.lower() == "norge":
    print("$0.44 per sang")
elif land.lower() == "sverige":
    print("$0.34 per sang")
else:
    print("$0 per sang")


antall_streams = int(input("Hvor mange streams har sangen"))
