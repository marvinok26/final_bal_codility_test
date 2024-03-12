def solution(A, D):
    balance = 0
    card_payments = 0
    card_payment_cost = 0
    monthly_fee = 5
    current_month = int(D[0].split('-')[1])
    month_count = {i: 0 for i in range(1, 13)}
    fee_paid = {i: False for i in range(1, 13)}

    for i in range(len(A)):
        balance += A[i]

        if A[i] < 0:
            card_payments += 1
            card_payment_cost -= A[i]

        month = int(D[i].split('-')[1])
        month_count[month] += 1

        if not fee_paid[month]:
            if month_count[month] >= 3 and card_payment_cost >= 100:
                fee_paid[month] = True
            else:
                balance -= monthly_fee

    if not fee_paid[12]:
        balance -= monthly_fee

    print(balance)

solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])
