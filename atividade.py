"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
def mergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        metadeEsq = lista[:meio]
        metadeDir = lista[meio:]

        mergeSort(metadeEsq)
        mergeSort(metadeDir)

        refEsquerda=0
        refDireita=0
        refLista=0
        while refEsquerda < len(metadeEsq) and refDireita < len(metadeDir):
            if metadeEsq[refEsquerda] < metadeDir[refDireita]:
                lista[refLista]=metadeEsq[refEsquerda]
                refEsquerda=refEsquerda+1
            else:
                lista[refLista]=metadeDir[refDireita]
                refDireita=refDireita+1
            refLista=refLista+1

        while refEsquerda < len(metadeEsq):
            lista[refLista]=metadeEsq[refEsquerda]
            refEsquerda=refEsquerda+1
            refLista=refLista+1

        while refDireita < len(metadeDir):
            lista[refLista]=metadeDir[refDireita]
            refDireita=refDireita+1
            refLista=refLista+1
            
    return lista


def mediana(lista1, lista2):

    lista3 = lista1 + lista2
    lista3 = mergeSort(lista3)

    if len(lista3)%2 == 0:
        i = int((len(lista3)-1)/2)
        j = i+1
        return (lista3[i]+lista3[j])/2
    else:
        i = int(len(lista3)/2)
        return lista3[i]



nums1=[1,3]
nums2=[2]

nums3=[3,4]
nums4=[1,2]

print(mediana(nums1,nums2))
print(mediana(nums3,nums4))
