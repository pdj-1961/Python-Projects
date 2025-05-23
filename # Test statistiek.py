# Test van verschillende statische methoden
import statistics

TestSet = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

print("Testset: ", TestSet)
print("Gemiddelde: ", statistics.mean(TestSet))
print("Mediaan: ", statistics.median(TestSet))
print("Modus: ", statistics.mode(TestSet))
print("Standaardafwijking: ", statistics.stdev(TestSet))
print("Variantie: ", statistics.variance(TestSet))
