def print_greeting():
    print("hello")
    print("bonjour")
    print("hola")


# עובד במפעלי ישראלקטריק חתום על הסכם השכר הבא:
#  אם הוותק מעל 10 שנים – תוספת של 10% משכר היסוד.
#  עבור כל ילד מהרביעי עד השישי (כולל) – תוספת של 400 ש"ח.
#  עבור כל ילד מהשביעי (כולל) – תוספת של 700 ש"ח.
#  כל שעה מעבר ל- 160 שעות  נחשבת "שעה נוספת".
#  עבור כל שעה נוספת מ- 16 הראשונות – 80 ש"ח.
#  עבור כל שעה נוספת מעבר לכך – 120 ש"ח.
#  קלוט משכורת יסוד, ותק, מספר ילדים ומספר שעות עבודה.
# תייצר פונקציה שמקבלת משכורת יסוד, ותק, מספר ילדים ומספר שעות עבודה כי פרמטרים ותחזיר את שכר המגיע לעובד מבלי לשנות את הקלט.
def calculate_salary(base_salary, seniority, child_num, work_hours):
    result = base_salary
    # seniority +10% if more than 10 years
    if seniority > 10:
        result *= 1.1
    # number of children
    if child_num > 7: #10
        # for each child after 7
        result += 700 * (child_num - 7)
        # for each child after 4
        result += 400 * 3
    elif 4 < child_num < 7:
        # for each child after 4
        result += 400 * (child_num - 4)
    # additional hours
    additional_hours = work_hours - 160
    if 0 < additional_hours <= 16:
        result += additional_hours * 80
    elif additional_hours > 16:
        result += 16 * 80
        result += (additional_hours - 16) * 120
    return result


# factorial recursion
def factorial(n): # 3, 2 , 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# entry point - the begging of the code
def main():
    # print_greeting()
    # print(calculate_salary(base_salary=3000, seniority=11, child_num=8, work_hours=250))
    int("abs")
    print(factorial(5))


















if __name__ == '__main__':
    main()