def raha_eurodes(aambrid, maasika_hind):
    hind_eurodes = maasika_hind / 100
    return aambrid * 5 * hind_eurodes

faili_nimi = input("Sisesta failinimi maasikate andmetega (strawberry_buckets.txt): ")
hind_sentides = int(input("Sisesta maasikate hind sentides: "))
kokku = 0

with open(faili_nimi, "r", encoding="utf-8") as f:
    for paev, rida in enumerate(f):
        rida = rida.strip()
        if rida:
            aambrite_arv = int(rida)
            tienitud = raha_eurodes(aambrite_arv, hind_sentides)
            kokku += tienitud
            print(f"{paev + 1}. päev teenitud {tienitud:.1f} eurot.")

print(f"Kogu teenitud raha: {kokku:.1f} eurot.")