# 上传到自己的 GitHub

## 1. 先完成个性化修改

上传之前至少修改以下两处：

1. 将 `README.md` 最后的作者信息改成你的姓名和 GitHub 地址。
2. 将 `LICENSE` 中的 `YOUR NAME` 改成你的英文姓名。

建议再做一项属于你自己的改进，例如：

- 加入月球和火星重力选项；
- 加入不同时间步长的误差比较；
- 增加速度随时间变化的图表；
- 将界面语言切换功能做成按钮。

面试时一定要能够解释你修改的功能和物理计算方法。

## 2. 在 GitHub 创建仓库

1. 登录 GitHub。
2. 选择 **New repository**。
3. Repository name 填写 `projectile-motion-simulator`。
4. Description 填写：

   `Interactive projectile motion simulator with quadratic air resistance.`

5. 选择 **Public**。
6. 不要勾选自动创建 README、LICENSE 或 `.gitignore`。

## 3. 使用终端上传

进入解压后的项目目录，然后执行：

```bash
git init
git add .
git commit -m "Create projectile motion simulator"
git branch -M main
git remote add origin https://github.com/你的用户名/projectile-motion-simulator.git
git push -u origin main
```

## 4. 后续提交示例

每增加一个功能，分别提交一次：

```bash
git add .
git commit -m "Add Mars gravity option"
git push
```

清晰的提交记录比一次性上传所有代码更能体现你的开发过程。

## 5. 面试时的日语说明

> 物理学で学んだ投射運動を題材に、PythonとStreamlitを使ってシミュレーションアプリを開発しました。空気抵抗を二次抵抗としてモデル化し、数値計算によって軌道を求めています。計算部分と画面部分を分離し、Pytestによるテストも実装しました。

不要说自己完全独立写出了所有内容。更稳妥的说法是：

> AIの支援も活用しましたが、物理モデルや各処理の意味を確認しながら実装し、自分でテストと修正を行いました。
