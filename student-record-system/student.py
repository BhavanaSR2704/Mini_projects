# Sample student data
students = [
    {"id": "1KI24IS006", "name": "Bhavana S R",   "dept": "ISE", "cgpa": 9.1, "year": 2},
    {"id": "1KI24IS058", "name": "Varsha D N",  "dept": "ISE", "cgpa": 8.5, "year": 2},
    {"id": "1KI24IS019", "name": "Hema D",    "dept": "ISE", "cgpa": 8.8, "year": 2},
    {"id": "1KI24CS050", "name": "Kanasu",      "dept": "CSE", "cgpa": 9.4, "year": 2},
    {"id": "1KI24CS004", "name": "Anju",     "dept": "CSE", "cgpa": 9.4, "year": 2},
    {"id": "1KI24CS059", "name": "Kushi",    "dept": "CSE", "cgpa": 9.5, "year": 2},
    {"id": "1KI24IS010", "name": "Chandana",   "dept": "ISE", "cgpa": 8.2, "year": 2},
    {"id": "1KI24IS015", "name": "Harish ",   "dept": "ISE", "cgpa": 9.0, "year": 2},
    {"id": "1KI24CS120", "name": "Ram",     "dept": "CSE", "cgpa": 8.6, "year": 2},
    {"id": "1KI24IS048", "name": "Raju",    "dept": "ISE", "cgpa": 7.2, "year": 2},
]

# ── Linear Search O(n) ──────────────────────────────────────────────
def linear_search(data, query):
    results = []
    for student in data:
        if (query in student['name'].lower() or
            query in student['id'].lower() or
            query in student['dept'].lower()):
            results.append(student)
    return results

# ── Bubble Sort O(n²) ───────────────────────────────────────────────
def bubble_sort(data, key='name', reverse=False):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = arr[j][key] if isinstance(arr[j][key], (int, float)) else arr[j][key].lower()
            b = arr[j+1][key] if isinstance(arr[j+1][key], (int, float)) else arr[j+1][key].lower()
            if (a > b) if not reverse else (a < b):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ── Quick Sort O(n log n) ───────────────────────────────────────────
def quick_sort(data, key='name', reverse=False):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2][key]
    pivot = pivot if isinstance(pivot, (int, float)) else pivot.lower()
    left   = [x for x in data if (x[key] if isinstance(x[key], (int,float)) else x[key].lower()) <  pivot]
    middle = [x for x in data if (x[key] if isinstance(x[key], (int,float)) else x[key].lower()) == pivot]
    right  = [x for x in data if (x[key] if isinstance(x[key], (int,float)) else x[key].lower()) >  pivot]
    sorted_ = quick_sort(left, key) + middle + quick_sort(right, key)
    return sorted_[::-1] if reverse else sorted_

# ── Merge Sort O(n log n) ───────────────────────────────────────────
def merge_sort(data, key='name', reverse=False):
    if len(data) <= 1:
        return data
    mid   = len(data) // 2
    left  = merge_sort(data[:mid], key, reverse)
    right = merge_sort(data[mid:], key, reverse)
    return merge(left, right, key, reverse)

def merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        a = left[i][key]  if isinstance(left[i][key],  (int,float)) else left[i][key].lower()
        b = right[j][key] if isinstance(right[j][key], (int,float)) else right[j][key].lower()
        if (a <= b) if not reverse else (a >= b):
            result.append(left[i]);  i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ── Binary Search O(log n) ─────────────────────────────────────────
def binary_search(sorted_data, query):
    results = []
    lo, hi = 0, len(sorted_data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        name = sorted_data[mid]['name'].lower()
        if name.startswith(query):
            results.append(sorted_data[mid])
            i = mid - 1
            while i >= 0 and sorted_data[i]['name'].lower().startswith(query):
                results.append(sorted_data[i]); i -= 1
            i = mid + 1
            while i < len(sorted_data) and sorted_data[i]['name'].lower().startswith(query):
                results.append(sorted_data[i]); i += 1
            break
        elif name < query:
            lo = mid + 1
        else:
            hi = mid - 1
    for s in sorted_data:
        if query in s['id'].lower() and s not in results:
            results.append(s)
    return results