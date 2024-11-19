from random import randint, seed, shuffle
words = [

  '2021182014', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 

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
    print('before :',words)
    count=len(words)
    mergesort(0,count-1)
    print('after: ' ,words)

def mergesort(left,right):
    if right <= left: return    # 정렬할 것이 없거나 하나뿐이면 정렬 X
    if right < left + 5:   #5개이하
        insertionSort(left,right)
        return
    mid = randint(left+1,right-1) ##파티션 랜덤으로 설정
    
    mergesort(left, mid)        # 왼쪽 정렬
    mergesort(mid+1, right)     #오른쪽 정렬
    merge(left, mid+1, right)


def merge(left,right,end):
    merged= [] #임시저장소
    i, r = left, right 
    while i<right and r<=end:
        if words[i]<=words[r]:
            merged.append(words[i])
            i+=1
        else :
            merged.append(words[r])
            r+=1

    while i<right:
        merged.append(words[i])
        i+= 1
    while r <= end:                    
        merged.append(words[r])          
        r += 1

    words[left:end+1] = merged  #임시저장소에 넣어놨던것들을 저장

def insertionSort(left, right):
    for i in range(left+1,right+1):
        v=words[i]
        j = i - 1
        while j >= left and words[j] > v:  #j가 처음 시작값보다 크거나 같고 v의 전 단어가 v보다 큰 경우
            words[j+1] = words[j]
            j -= 1
        words[j+1] = v


main()