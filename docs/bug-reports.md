# Баг-репорты - DemoBlaze
- **URL:** https://www.demoblaze.com/index.html  
- **Дата:** 06.09.2026 
- **Окружение:** Windows 11, Chrome 152.0.7977.77

## Сводка

### Количество багов
- **Всего:** 4
- **Critical:** 1
- **Major:** 3
- **Open:** 4

### Таблица багов
| ID | Модуль | Название (кратко) | Severity | Priority | Статус |
|---|---|---|---|---|---|
| BUG-AUTH-001 | Authentication / Sign up | Username из пробелов → неверное сообщение `This user already exist.` | Major | Medium | Open |
| BUG-CHK-001 | Checkout / Place Order | Credit card принимает буквы и оформляет заказ | Critical | High | Open |
| BUG-CONT-001 | Contact form | Отправка сообщения с пустым Email | Major | Medium | Open |
| BUG-CONT-002 | Contact form | Отправка сообщения с невалидным Email (без `@`) | Major | Medium | Open |

---

## BUG-AUTH-001
- **Название:** Sign up: при вводе username из пробелов показывает неверное сообщение "This user already exist." 
- **Связанный тест-кейс:** TC-AUTH-12
- **Модуль:** Authentication / Sign up
- **Severity:** Major
- **Priority:** Medium
- **Статус:** Open

### Предусловия
- Пользователь не залогинен
- Открыто модальное окно **Sign up**

### Шаги воспроизведения
1. В поле **Username** ввести `     ` (5 пробелов)
2. В поле **Password** ввести `Test123!`
3. Нажать **Sign up**

### Ожидаемый результат
- Регистрация не выполнена
- Показано корректное сообщение валидации 
- Username не должен приниматься, если состоит только из пробелов

### Фактический результат
- Показано alert-сообщение `This user already exist.`
- Сообщение валидации для некорректного username не отображается
- Регистрация не завершается (аккаунт не создаётся)

### Дополнительные замечания
Сообщение `This user already exist.` не соответствует введённым данным и может вводить пользователя в заблуждение (проблема в невалидном username, а не в существующем аккаунте).

### Evidence
- `evidence/screenshots/BUG-AUTH-001_spaces_username.png` (форма Sign up с 5 пробелами в Username)
- `evidence/screenshots/BUG-AUTH-001_alert.png` (alert с текстом)

---

## BUG-CHK-001
- **Название:** Checkout: поле Credit card принимает буквы и позволяет оформить заказ
- **Связанный тест-кейс:** TC-CHK-03
- **Модуль:** Checkout / Place Order
- **Severity:** Critical
- **Priority:** High
- **Статус:** Open

### Предусловия
- В корзине есть товар
- Открыта форма **Place Order**

### Шаги воспроизведения
1. Заполнить форму валидными данными 
2. В поле **Credit card** ввести `abcd1234`
3. Нажать **Purchase**

### Ожидаемый результат
- Заказ не оформлен
- Показано сообщение об ошибке формата (Credit card должен содержать только цифры)

### Фактический результат
- Сообщение об ошибке не показано
- Заказ оформлен 

### Evidence
- `evidence/screenshots/BUG-CHK-001_form_filled.png` (форма с введенным `abcd1234`)
- `evidence/screenshots/BUG-CHK-001_purchase_success.png` (подтверждение покупки)

---

## BUG-CONT-001
- **Название:** Contact: отправка сообщения возможна при пустом Email
- **Связанный тест-кейс:** TC-CONT-01
- **Модуль:** Contact form
- **Severity:** Major
- **Priority:** Medium
- **Статус:** Open

### Предусловия
- Открыто модальное окно **Contact**

### Шаги воспроизведения
1. Оставить поле **Contact Email** пустым
2. Заполнить **Contact Name** любым текстом 
3. Заполнить **Message** любым текстом 
4. Нажать **Send message**

### Ожидаемый результат
- Сообщение не отправлено
- Показана ошибка/alert о необходимости заполнить Email

### Фактический результат
- Ошибка не показана
- Сообщение отправлено, показано success alert
### Evidence
- `evidence/screenshots/BUG-CONT-001_empty_email.png` (пустой Email)
- `evidence/screenshots/BUG-CONT-001_success_alert.png` (success alert)

---

## BUG-CONT-002
- **Название:** Contact: отправка сообщения возможна с невалидным Email (без символа @)
- **Связанный тест-кейс:** TC-CONT-02
- **Модуль:** Contact form
- **Severity:** Major
- **Priority:** Medium
- **Статус:** Open

### Предусловия
- Открыто модальное окно **Contact**

### Шаги воспроизведения
1. Ввести Email: `testtest.com` (без `@`)
2. Ввести **Contact Name** любым текстом 
3. Ввести **Message** любым текстом 
4. Нажать **Send message**

### Ожидаемый результат
- Сообщение не отправлено
- Показана ошибка о некорректном формате email

### Фактический результат
- Ошибка не показана
- Сообщение отправлено, показано success alert 
### Evidence
- `evidence/screenshots/BUG-CONT-002_invalid_email.png` (email `testtest.com`)
- `evidence/screenshots/BUG-CONT-002_success_alert.png` (success alert)

