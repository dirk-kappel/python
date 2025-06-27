import createPHZ
import discoverEndpoints

endpoints = discoverEndpoints.main()
# print(endpoints)
# print()

privateHostedZones = createPHZ.main(endpoints)
# print('-'*30)
# print(privateHostedZones)
