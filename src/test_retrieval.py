from retrieve_faers import search_faers

results = search_faers(
    "ibuprofen headache"
)

print()

print("FDA Results")

print()

for r in results:
    print(r)