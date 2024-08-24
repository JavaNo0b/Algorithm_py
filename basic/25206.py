#심화1-너의 평점은
unitSum = 0.0
scoreSum = 0.0

def grade_to_score(rating):
  if rating == "A+":
    return 4.5
  elif rating == "A0":
    return 4.0
  elif rating == "B+":
    return 3.5
  elif rating == "B0":
    return 3.0
  elif rating == "C+":
    return 2.5
  elif rating == "C0":
    return 2.0
  elif rating == "D+":
    return 1.5
  elif rating == "D0":
    return 1.0
  else:
    return 0.0


for i in range(20):
  subDetail = input().split()
  unit = float(subDetail[1])
  rating = subDetail[2]
  if rating == "P":
    continue
  else:
    score = grade_to_score(rating)
    unitSum += unit
    scoreSum += unit*score

final_score = scoreSum / unitSum
print(f"{final_score:.4f}")