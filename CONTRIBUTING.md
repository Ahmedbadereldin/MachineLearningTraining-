## 🔒 Branch Protection Guidelines | إرشادات حماية الفروع

To ensure a clean and collaborative development process, **no one is allowed to push directly to the `development` branch**.  
All updates must go through **Pull Requests (PRs)**.

لضمان سير العمل بطريقة منظمة وتعاونية، **ممنوع تماماً عمل push مباشر على فرع `development`**.  
يجب إرسال التعديلات عبر **طلبات السحب (Pull Requests - PRs)** فقط.

---

### ✅ Enforced Rules | القواعد المطبقة:

- 🔁 **Pull Request is required** before merging to `development`.
- 👥 **At least one code review approval** is required before merging.
- 🛡️ **Pushes to `development` are restricted** for all contributors.
- 🔍 **(Optional)** Status checks must pass before merging (e.g., tests, linting).
- 🧑‍💼 (Optional) Even **admins must follow these rules**.

---

### 📌 How to contribute | طريقة المساهمة:

1. Create a new feature or fix branch from `development`:  
   ```bash
   git checkout -b feature/my-feature development
   ```

2. Make your changes and commit.

3. Push your branch to GitHub:
   ```bash
   git push origin feature/my-feature
   ```

4. Open a Pull Request **from your branch → to `development`**.

---

Thank you for keeping our repo clean and collaborative! 🤝  
شكرًا لالتزامك بسير العمل المنظم والتعاوني في المشروع!
