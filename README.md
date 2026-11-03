# QA Pet Project — DemoBlaze & ReqRes (Manual + Automation)

Учебный пет-проект, объединяющий ручное тестирование e-commerce (DemoBlaze), автоматизацию UI/API (ReqRes) и CI/CD через GitHub Actions.

* **Тестирование UI:** [DemoBlaze](https://demoblaze.com)
* **Тестирование API:** [ReqRes.in](https://reqres.in)
* **Формат:** Ручное тестирование + Автоматизация (Python/Pytest) + CI/CD

---

## Документация

* `docs/test-plan.md` — Тест-план
* `docs/smoke-checklist.md` — Чек-лист проверки
* `docs/test-cases.md` — Сценарии для ручных проверок
* `docs/bug-reports.md` — Найденные баги
* `docs/automation.md` — **[NEW]** Руководство по автотестам
* `docs/api-testing.md` — Спецификация проверок бэкенда

### Вложения
* Скриншоты и баги: `evidence/screenshots/`

---

## Краткая сводка по результатам

* **Smoke / Функциональные тесты:** Пройдены/найдены дефекты 
* **API / UI E2E автотесты:** Успешно запущены
* **Найдено багов:** 4 дефекта

---

## Стек технологий в автоматизации

* **Язык / Фреймворк:** Python 3.13, Pytest
* **Инструменты:** Playwright (UI), Requests (API), GitHub Actions (CI/CD)

---

## Как пользоваться репозиторием

1. **Ручное тестирование:** см. `docs/test-plan.md` и `docs/bug-reports.md`.
2. **Автоматизация:** см. `docs/automation.md` или запустите `pytest -v`.
