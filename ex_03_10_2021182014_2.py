from random import randint, seed, shuffle

words = [    '2021182014', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 
    'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy', 
   'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft', 
   'temporize', 'speedboat', 'agenda', 'delusion', 'addle', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 
   'quite', 'seminar', 'bloomers', 'lives', 'innocuous', 'effluent', 'cross', 'recidivist', 'wet', 'synth', 
   'mantilla', 'tweak', 'lowbrow', 'aviation', 'quadruped', 'capable', 'graphic', 'barman', 'intemperate', 'mastermind', 
   'submit', 'considering', 'riddance', 'polyethene', 'jim', 'varicolored', 'medic', 'ferric', 'minaret', 'capacitor', 
   'pusher', 'gingerbread', 'grizzled', 'upsilon', 'km', 'glade', 'ribbon', 'parascending', 'shinty', 'breve', 
   'hotel', 'similitude', 'fuddle', 'secretariat', 'silicate', 'whinchat', 'abstention', 'untrue', 'toing', 'cnd', 
   'ramification', 'scorn', 'apricot', 'arnica', 'militate', 'muslim', 'homicide', 'overfeed', 'shooting', 'growth', 
]

def main():
    print('before quick sort:', words)
    
    count = len(words)
    quickSort(words,0, count-1)
    insertionSort(words,0, count-1)
    
    print('after quick sort:', words)

def quickSort(arr,left, right):
    if left <= right:
        return
    if right < left + 5:   #5개 이하
        insertionSort(left+1,right-1)
        return
    pivot = partition(left, right)
    
    quickSort(arr,left, pivot-1)
    quickSort(arr,pivot+1, right)
    
def insertionSort(arr,left, right):
    for i in range(left+1, right+1):
        v = words[i]
        j = i - 1
        while j >= left and words[j] < v:  # 내림차순이므로 '>' 대신 '<' 사용
            words[j+1] = words[j]
            j -= 1
        words[j+1] = v

def partition(left, right):
    pi = left               # pi = Pivot Index
    pivot = words[pi]       # pivot = value
    p, q = left, right + 1  # 후보 선수들 출전 준비
    while True:             # p와 q가 역전할 때까지
        while True:         # 왼쪽에서 pivot보다 작은 값을 찾을 때까지
            p += 1
            if q < p: break
            if p > right or words[p] <= pivot: break  # '<='으로 변경

        while True:         # 오른쪽에서 pivot보다 큰 값을 찾을 때까지
            q -= 1
            if q < p: break
            if words[q] >= pivot: break  # '>='으로 변경

        if p >= q: break
        # p와 q가 만날 때까지 계속 진행
        words[p], words[q] = words[q], words[p]

    if left != q:
        words[left], words[q] = words[q], words[left]
    return q

main()
