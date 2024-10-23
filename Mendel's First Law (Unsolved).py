k,m,n = map(int, input("Enter 3 digits k, m, and n, representing different genomes: ").split())
total = k + m + n
# k has a probability of 1 with all groups
# m has a probability of 1 if mating with dominant, .75 if with other heterozygous, .5 if mating with homozygous recessive
# n has a probability of 0 when mating with other homozygous recessive
# script doesn't work proberly (because i'm bad at probability calculations)
probability = ((k/total) + (((k-1)/(total-1))) * 1) * (((k/total) + (m/total)) * 1 ) * (((k/total) + (n/total)) * 1 ) * (((m/total) + ((m-1)/(total-1))) * .75 )+ (((m/total) + (n/total)) * .5) * (((n/total) + ((n-1)/(total-1))) * 0)
print(probability)