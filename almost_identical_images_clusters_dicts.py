

# We have a pipeline, which produces a mapping from every image to a list of up to k near-duplicate images, such as:
# near_dups = {
# "A": ["B", "I", "K"],
# "B": ["A", "D"],
# "C": ["E"],
# "D": [],
# "E": [],
# "F": [],
# "G": ["K"],
# "I": [],
# "K": [],
# }
# Given a mapping such as this one, form clusters: collections of almost identical images.
# In the example above, we would form the following groups: (A, B, D, I, G, K), (C, E), and (F).**

near_dups = {
    "A": ["B", "I", "K"],
    "B": ["A", "D"],
    "C": ["E"],
    "D": [],
    "E": [],
    "F": [],
    "G": ["K"],
    "I": [],
    "K": [],
}

imgs_to_check = list(near_dups.keys())

img_clusters = []
curr_cluster = []
to_check_queue = []

while len(imgs_to_check) > 0:
    print()
    print(f'near_dups: {near_dups}')
    print(f'imgs_to_check: {imgs_to_check}')
    print(f'to_check_queue: {to_check_queue}')
    print(f'curr_cluster: {curr_cluster}')
    if len(to_check_queue) == 0:
        if len(curr_cluster) > 0:
            print(f'Cluster completed: {curr_cluster}')
            img_clusters.append(curr_cluster)
        img_to_check = imgs_to_check.pop(0)
        curr_cluster = [img_to_check]
        img_to_check_dups = near_dups.pop(img_to_check)
        if len(img_to_check_dups) > 0:
            to_check_queue += img_to_check_dups
    else:
        now_checking = to_check_queue.pop(0)
        imgs_to_check.remove(now_checking)
        curr_cluster.append(now_checking)
        img_to_check_dups = near_dups.pop(now_checking)
        if len(img_to_check_dups) > 0:
            for img in img_to_check_dups:
                if img not in to_check_queue and img in imgs_to_check:
                    to_check_queue.append(img)

print()
print(f'near_dups: {near_dups}')
print(f'imgs_to_check: {imgs_to_check}')
print(f'to_check_queue: {to_check_queue}')
print(f'curr_cluster: {curr_cluster}')
if len(to_check_queue) > 0:
    now_checking = to_check_queue.pop(0)
    curr_cluster.append(now_checking)
    print(f'Cluster completed: {curr_cluster}')
    img_clusters.append(curr_cluster)

print(f'Final clusters are: {img_clusters}')
