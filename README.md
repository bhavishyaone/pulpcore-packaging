# 🎩 pulpcore RPM Packaging

Welcome to **Pulpcore's** RPM packaging repository! Here, you’ll find RPM spec files for various **Pulpcore** versions, organized for seamless building, deploying, and integration with **Katello** installations. Let’s dive into the essentials!

---

### 🌐 Default Branch  
> The default branch always points to the **latest packaged version** of Pulpcore, so you’re always up to date.

---

### 🛠 Requirements  
**For Basic Contributions**  
No special setup is required—jump right in and submit your fixes!  

**For Building or Releasing RPMs**  
You'll need:
- **[obal](https://github.com/theforeman/obal)**  (v0.10.0 or higher)
- **[mock](http://fedoraproject.org/wiki/Projects/Mock)** or **koji client**  
  _(Ensure you have an account with a certificate on [koji.katello.org](https://koji.katello.org))_

---

### 📦 Repository & Katello Integration  
The RPMs created with this repository are deployed to:

**[yum.theforeman.org/pulpcore](https://yum.theforeman.org/pulpcore/)**

These are directly integrated within **Katello** installations through the `katello-repos` RPM package.

---

### 📄 License  
Unless otherwise specified, these spec files are based on Fedora's and are available under the **MIT License**.
