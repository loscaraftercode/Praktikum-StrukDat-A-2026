class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def tampilkan_antrean(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def sisipkan_vip(head, plat_baru, plat_target):
    currentNode = head


    while currentNode:
        if currentNode.data == plat_target:
            break
        currentNode = currentNode.next


    if currentNode is None:
        print("Plat target tidak ditemukan!")
        return head


    newNode = Node(plat_baru)


    newNode.next = currentNode.next
    currentNode.next = newNode

    return head



node1 = Node("BM1234AA")
node2 = Node("BM2345BB")
node3 = Node("BM3456CC")
node4 = Node("BM4567DD")

node1.next = node2
node2.next = node3
node3.next = node4

print("Antrean awal:")
tampilkan_antrean(node1)


node1 = sisipkan_vip(node1, "BM9999VIP", "BM2345BB")

print("\nAntrean setelah VIP disisipkan:")
tampilkan_antrean(node1)