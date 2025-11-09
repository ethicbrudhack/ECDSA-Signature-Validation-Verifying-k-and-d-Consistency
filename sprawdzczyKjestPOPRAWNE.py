from ecdsa.numbertheory import inverse_mod
from ecdsa.ecdsa import generator_secp256k1

# ✅ Twoje dane
r = int("89468bb80547d34a6a3bdaa6bdbbca688fface3a8769ec07fac39aee56796b46", 16)
s = int("599fc0aaae7952b6adf65140fbd1b9221ba5d6a32afdebcbd927a3b59fd637be", 16)
z = int("37541378882d53d59d9ecb80ccd6f72e978117845a250337e92351cac498c180", 16)
k = int("aabae116f4f5263f049dd6a1c54a88b6df0f43d2909873b8114d679c5b6430bd", 16)
d = int("c263c7d05ff8529c60993d350f34dd2b8dbf37eb2e3c7c49fac85d45188073ac", 16)

# ✅ Stała wartość krzywej secp256k1 (order n)
n = generator_secp256k1.order()

# ✅ Oblicz `s_test` na podstawie wzoru ECDSA
k_inv = inverse_mod(k, n)  # Obliczamy odwrotność `k`
s_test = (k_inv * (z + d * r)) % n

# ✅ Sprawdzenie, czy `s_test` == `s`
print(f"🚀 ✅ Obliczone s: {hex(s_test)}")
print(f"📌 🔹 Oryginalne s: {hex(s)}")

if s_test == s:
    print("✅ 🔥 `k` jest poprawne!")
else:
    print("❌ `k` jest niepoprawne. Może błąd w obliczeniach `k` lub `d`.")
