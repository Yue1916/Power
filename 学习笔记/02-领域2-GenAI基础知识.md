# 内容领域 2：GenAI 基础知识（占计分内容 24%）

## 领域概述（学习地图）

领域 2 在领域 1 的基础上，聚焦**生成式 AI (GenAI)**，占计分内容 **24%**（第二高）。分三个任务陈述：

- **任务 2.1 解释 GenAI 的基本概念**：AI 与 GenAI 的定义和区别；GenAI 的使用案例；**基础模型 (FM) 生命周期**；Token/嵌入/向量/Transformer/多模态/扩散模型等核心术语。
- **任务 2.2 GenAI 的能力与局限**：GenAI 的**优势与风险**；选择模型要考虑的因素；如何用**指标**衡量业务价值。
- **任务 2.3 构建 GenAI 应用的 AWS 基础设施与技术**：可用的 **AWS 服务与功能**；用 AWS GenAI 服务的**优势与成本权衡**。

> 与领域 1 的衔接：领域 1 讲"AI/ML 是什么、怎么建"，领域 2 专门深入"**生成式** AI"——即**创造新内容**（文本/图像/音视频/代码），而不是分类或预测。

---

## 任务说明 2.1：解释生成式人工智能（GenAI）的基本概念

**官方目标：**
- 定义 GenAI 基础概念（Token、分块、嵌入、向量、提示工程、基于 Transformer 的 LLM、基础模型 FM、多模态模型、扩散模型）
- 确定 GenAI 模型的潜在使用案例（图像/视频/音频生成、摘要、AI 助手、翻译、代码生成、客服代理、搜索、推荐引擎）
- 描述 FM 生命周期（数据选择、模型选择、预训练、微调、评估、部署、反馈）
- 描述基于令牌的定价模型及其对推理成本和性能的影响
- 描述上下文工程在 FM 应用中的作用
- 定义基础的智能体 AI 概念（多智能体系统模式、模型上下文协议 [MCP]、多智能体通信模式、内存管理、工具使用、工作流编排）

### 🌱 一句话入门（零基础先看这里）

**生成式 AI = 深度学习的一个子集，专门"创造新的原创内容"**（文本、图像、音频、视频、代码），而不是像普通 AI 那样"分类"或"预测"。

- 它靠**基础模型 (Foundation Model, FM)**——一种**超大神经网络**，用海量数据预训练、有**数十亿参数**。
- 你给它一段输入（**提示词 prompt**），它一个词一个词地"猜"下一个该输出什么，拼成回答（**补全 completion**）。
- 底层技术是 **Transformer**（2017 论文《Attention Is All You Need》），靠**自注意力**理解上下文。

**类比**：普通 AI 像"判卷老师"（判断对错、归类）；生成式 AI 像"作家/画家"（写出、画出新东西）。

> 这个任务要掌握：GenAI 是什么、怎么工作（Token→向量→嵌入→自注意力）、有哪些用例、FM 生命周期、以及单模态/多模态/扩散模型的区别。

### 视频学习笔记

> 本任务共 5 节课。

---

> **第 1 课：什么是生成式 AI + 核心概念**

#### 1. GenAI 的定位与特点

- **GenAI 是深度学习的子集**：多用途技术，用于**生成新的原创内容**（文本、图像、音频、视频、代码），而非查找/分类现有内容。
- 对比：普通 AI 侧重**分类/预测**；GenAI 侧重**创造**。
- 工作方式：从大量训练数据中**学习模式和表示**，再生成与训练数据相似的输出。

#### 2. 基础模型 (Foundation Model, FM)

- 基于**海量数据**训练、在自然语言/图像等形式中找**统计模式**的**超大复杂神经网络**。
- 有在（预）训练阶段学到的**数十亿参数**；**参数越多 → 占用内存越大、能执行越高级的任务**。
- 用法：**原样直接用**，或用**微调 (fine-tuning)** 按特定用例调整。
- 模型由**神经网络 + 系统资源 + 数据 + 提示词**协同构成；输出本质是**对"下一个词/分词"的猜测**。

#### 3. Transformer 是 GenAI 的核心

- 出自 2017 论文**《Attention Is All You Need》**；ChatGPT 等 LLM 都基于 Transformer。
- LLM 用互联网海量文本**预训练**建立广泛知识库，再用**少量额外数据微调**到特定任务。
- GenAI LLM 能接受**自然语言指令**并像人一样执行任务。

#### 4. 必记核心术语（考试点名）

- **提示词 (Prompt)**：你发给模型的输入（文本，也可用于图像/视频等）。
- **推理 (Inference)**：把提示词传入模型生成输出的过程。
- **补全 (Completion)**：模型对提示词生成的输出。
- **上下文窗口 (Context Window)**：模型一次能处理的输入长度范围。
- **分词 (Token) / 分词器 (Tokenizer)**：把文本切成 Token；分词器把人类文本转成 Token。
- **LLM 词汇表 (Vocabulary)**：模型认识的所有 Token 集合。
- **提示词工程 (Prompt Engineering)**：调整提示词以获得更好输出的技巧。
- 底层计算：概率建模、损失函数、矩阵乘法（ML 更擅长处理数字而非原始文本/图像）。

#### 5. 上下文学习 (In-context Learning)

- 在**提示词里加入示例或额外数据**，帮助 LLM 更好理解任务——即"上下文学习"。
- 三种"样本"方式（在上下文窗口内提供示例的数量）：
  - **零样本 (Zero-shot)**：不给示例。
  - **单样本 (One-shot)**：给 1 个示例。
  - **少样本 (Few-shot)**：给几个示例。
- **推理配置参数**会影响补全效果（后面 3.1 细讲，如温度）。

---

> **第 2 课：向量、嵌入与自注意力（GenAI 怎么"懂"语言）**

#### 1. 向量 (Vector)

- 定义：一个**有序的数字列表**，表示某实体/概念的特征或属性；也表示该列表在**空间中的位置**（类比：Excel 里行号+列号定位一个单元格）。
- 在 GenAI 中，向量可表示单词、短语、句子等，并能**编码项目间的关系**（类比、层次）。例：海牛↔儒艮 的向量差，类似 无沟双髻鲨↔双髻鲨 的差。

#### 2. 嵌入 (Embedding)

- **分词器**先把输入文本转成带 **Token ID（输入 ID）** 的向量，每个 ID 对应词汇表里一个 Token。
- **嵌入 (Embedding)** = 每个 Token 的**高维向量化表示**，捕获文本/图像/视频/音频的**语义含义**。
- **向量空间中越接近 → 语义越相似**；模型据此生成文本。

#### 3. 自注意力 (Self-Attention)——Transformer 的关键创新

- 生成每个输出 Token 时，**权衡输入不同部分的重要性** → 捕获 **RNN 难以学习的长距离依赖和上下文关系**。
- 机制：为每个 Token 算**查询 Query / 键 Key / 值 Value** 向量 → 用 Q·K 点积得**注意力权重** → 输出是 Value 的**加权和**；多层重复，构建复杂表示。
- **位置嵌入 (Positional Embedding)**：编码每个 Token 在序列中的**相对位置**，帮助区分相同 Token 在不同位置的含义（理解词序/句子结构）。

#### 4. Transformer 结构回顾

- 由**编码器 (Encoder) + 解码器 (Decoder)** 组成，各含多层、每层两个子层。
- 用**残差连接**和**层规范化**促进训练、防过拟合；用**位置编码**记录顺序（无需循环/卷积）。
- 相比 RNN/CNN，能**并行化计算 + 捕获长距离依赖**，在机器翻译等任务上表现更好。
- 流程链：输入 → 嵌入层 → 编码器/自注意力 → 解码器 → **Softmax 输出**（概率分布选下一个 Token）。

---

> **第 3 课：规模、预训练、单模态 vs 多模态、扩散模型**

#### 1. 模型规模与"涌现"

- 模型越大，**无需额外上下文学习或训练就能工作**的可能性越大 → 推动开发越来越大的模型。
- 但训练大模型**又难又贵**，无法无限增大。

#### 2. 预训练 (Pre-training) 深入

- LLM 在预训练阶段从**海量非结构化数据**（GB/TB/PB 级，来自网络抓取和专门语料）中，**自监督学习 (self-supervised)** 语言的模式和结构。
- 预训练中**更新模型权重以最小化训练目标的损失**；编码器为每个 Token 生成嵌入；需要**大量算力和 GPU**。
- 数据要**处理**（提质、去偏差、删有害内容）；据估**仅 1%~3% 的 Token** 在质量策管后用于预训练——估算自建模型需多少数据时要考虑这点。

#### 3. 单模态 vs 多模态 (Unimodal vs Multimodal)

- **单模态**：只处理一种模态。**LLM 是单模态示例**（输入输出都是文本）。
- **多模态**：加入图像/视频/音频等多种模态；能理解多种数据源，预测更可靠。
- 多模态用例：营销、图像字幕、产品设计、客服、聊天机器人、虚拟化身；任务如**图像字幕、可视化问答 (VQA)、文本到图像合成**（DALL-E、Stable Diffusion、Midjourney）。

#### 4. 扩散模型 (Diffusion Models)

- 一类生成模型，**学习"反转一个逐步加噪的过程"**：从随机噪声出发，通过**迭代降噪**生成连贯输出（高质量图像/音频）。
- 三个主要组成（考点）：**正向扩散、反向扩散、稳定扩散 (Stable Diffusion)**。
- **Stable Diffusion**：不在图像的**像素空间**操作，而在简化的**隐空间 (latent space)**；可通过 **SageMaker JumpStart** 用文本生成图像。
- **相比 GAN / VAE 的优势**：输出质量更高、多样性和一致性更好、更稳定更易训练。
- 示例：Stable Diffusion（图像）、Whisper（语音识别/翻译）、AudioLM（音频生成）。
- AWS：SageMaker 支持 TensorFlow/PyTorch，提供 Stable Diffusion 等预训练模型可微调部署。

---

> **第 4 课：生成任务与使用案例**

#### 1. LLM 的通用性

- LLM 是一种 GenAI，**无需微调即可应用于许多不同任务/领域**。

#### 2. 主要使用案例（用例记忆库）

- **文本生成/改写**：面向不同受众改写（如把水肺潜水技术文档改成少术语的入门版）。
- **文本摘要**：长文压成保留主旨的短文（技术文档、财报、法律文件、新闻）。
- **代码生成**：按自然语言描述生成代码片段/整段程序、补全代码、跨语言翻译代码。
- 其他：信息提取、问答、分类、识别有害内容、翻译、推荐引擎、个性化营销广告、聊天机器人、客服座席、搜索。

#### 3. 对应 AWS 服务

- **Amazon Bedrock + Amazon Titan**：文本/图像/音频生成的预训练模型，可微调。
- **Amazon Q Developer**（原 CodeWhisperer）：实时代码建议（片段到完整函数），基于你的注释和现有代码。
- **Amazon Nimble Studio / Amazon Sumerian**：虚拟制作、3D 内容创作。

#### 4. 三种生成式架构（考点）

- **生成式对抗网络 (GAN)**、**变分自编码器 (VAE)**、**Transformer**——各有优劣，选型前先评估目标和数据集。

---

> **第 5 课：生成式 AI 项目生命周期**

#### 1. 两套生命周期（都要眼熟）

**GenAI 项目生命周期（本课框架）：**
```
确定使用案例 → 实验并选择 → 适应/调整/增强 → 评估/部署/迭代 → 监控
```

**基础模型 (FM) 生命周期（考试指南列出，必记）：**
```
数据选择 → 模型选择 → 预训练 → 微调 → 评估 → 部署 → 反馈
```

#### 2. 各阶段要点

- **确定使用案例（最重要）**：尽量**精确、狭义**地定义范围。想清楚 LLM 在应用里扮演什么角色——是要多任务通用能力（含长文本生成），还是只需擅长一件事（如命名实体识别 NER）？**范围越具体，越省时间和计算成本**。
- **实验并选择**：先决定**从头训练**还是**用现成 FM**（通常用现成的）。
- **适应/调整/增强（高度迭代）**：优先级顺序——
  1. 先试**提示词工程 + 上下文学习**（零/单/少样本）；
  2. 不够好再**微调 (fine-tuning)**（有监督学习过程）；
  3. 用 **RLHF（基于人类反馈的强化学习）** 让输出更符合人类偏好；
  4. 全程用**评估**（不同指标和基准）衡量表现和与偏好的一致性。
- **部署**：部署到基础设施、与应用集成，优化模型和计算资源，保证用户体验；考虑运行所需的其它基础设施。

#### 3. LLM 的基本局限（仅靠训练难以完全克服）

- **幻觉 (Hallucination)**：不知道答案时**编造信息**。
- **复杂推理和数学能力有限**。

#### 📎 补充资料（额外阅读）：GAN 深入

> 来源：AWS "What is a GAN?" 官方文章整理。

**GAN（生成式对抗网络）= 两个神经网络对抗训练**
- **生成器 (Generator)**：拿输入样本、尽量修改，**制造以假乱真的新数据**。
- **判别器 (Discriminator)**：判断收到的数据是**真的（属于原数据集）还是假的（生成的）**。
- **对抗过程**：生成器想"骗过"判别器，判别器想"识破"；两者反复迭代进化，直到达到**平衡 (equilibrium)**——判别器再也分不出真假，训练结束。
- 记忆：**生成器造假、判别器打假，越练越强**。

**GAN 的用例**
- 生成逼真**图像**（文本→图像、低分辨率→高分辨率、黑白→彩色）；
- 生成**训练数据**（数据增强，如造假交易数据训练欺诈检测模型）；
- **补全缺失信息**；从 2D 生成 **3D 模型**（如医疗器官建模）。

**GAN 类型（认识名字即可）**
- **Vanilla GAN**：最基础版。
- **Conditional GAN (cGAN)**：加入**条件**（如类别标签）做**定向生成**。
- **DCGAN**：融合 **CNN**（卷积），更适合图像、训练更稳定。
- **SRGAN**：**超分辨率**，把低清放大成高清。

> 对比记忆：**GAN**（对抗）、**VAE**（变分自编码器）、**扩散模型**（加噪降噪）、**Transformer**（自注意力）——都是生成式架构，扩散模型通常质量/稳定性更优。

### ⚠️ 视频未覆盖 / 需补充（对照考纲）

官方目标 2.1 还包含几个**视频没展开**的点，补充如下（部分会在领域 2/3 深入）：

- **基于令牌的定价模型 (Token-based Pricing)**：GenAI 服务（如 Bedrock）常**按处理的 Token 数计费**（输入 Token + 输出 Token 分别计价）。影响：**提示词越长、输出越长 → 成本越高、延迟越大**。优化：精简提示、限制最大输出长度、用 Prompt 缓存。
- **上下文工程 (Context Engineering)**：比"提示词工程"更广，指**系统性地组织喂给模型的上下文**（指令 + 示例 + 检索到的知识 + 历史对话等），让 FM 在有限上下文窗口内拿到**最相关**的信息。RAG 是其典型手段。
- **智能体 AI (Agentic AI) 基础概念**（领域 3 会细讲，这里先建立印象）：
  - **多智能体系统 (Multi-agent Systems)**：多个 AI 智能体协作完成复杂任务。
  - **模型上下文协议 (MCP, Model Context Protocol)**：一种**标准协议**，让智能体**连接外部系统/工具/数据源**。
  - **多智能体通信模式**：智能体之间如何协调、传递信息。
  - **内存管理 (Memory Management)**：智能体记住上下文/历史。
  - **工具使用 (Tool Use)**：智能体调用外部工具/API 完成动作。
  - **工作流编排 (Workflow Orchestration)**：编排多步骤任务的执行顺序。

### 关键术语速记

> 术语以「中文 (English)」对照。

**核心概念**
- **生成式 AI (Generative AI, GenAI)**：深度学习子集，生成新原创内容。
- **基础模型 (Foundation Model, FM)**：海量数据预训练、数十亿参数的超大模型。
- **大型语言模型 (Large Language Model, LLM)**：以文本为输入输出的单模态 FM。
- **Transformer**：GenAI 核心架构，靠自注意力；出自《Attention Is All You Need》(2017)。

**输入输出流程**
- **提示词 (Prompt) → 推理 (Inference) → 补全 (Completion)**：输入 → 计算 → 输出。
- **上下文窗口 (Context Window)**：一次可处理的输入长度。
- **分词 (Token) / 分词器 (Tokenizer) / 词汇表 (Vocabulary)**。
- **Token ID / 输入 ID (Input ID)**：Token 在词汇表中的编号。

**向量与注意力**
- **向量 (Vector)**：有序数字列表，表示特征与空间位置。
- **嵌入 (Embedding)**：Token 的高维向量表示，捕获语义；越近越相似。
- **自注意力 (Self-Attention)**：用 **查询 Query / 键 Key / 值 Value** 权衡各 Token 重要性，捕获长距离依赖。
- **位置嵌入/编码 (Positional Embedding / Encoding)**：编码 Token 顺序。
- **编码器 (Encoder) / 解码器 (Decoder) / Softmax 输出**。

**学习与生成方式**
- **上下文学习 (In-context Learning)**：提示词里加示例。
- **零样本 / 单样本 / 少样本 (Zero-/One-/Few-shot)**。
- **提示词工程 (Prompt Engineering) / 上下文工程 (Context Engineering)**。
- **预训练 (Pre-training)**：自监督学习海量数据、更新权重。
- **微调 (Fine-tuning) / RLHF（基于人类反馈的强化学习）**。

**模型类别**
- **单模态 / 多模态 (Unimodal / Multimodal)**：LLM 是单模态；多模态含图像/音视频。
- **扩散模型 (Diffusion Model)**：加噪→迭代降噪生成；正向/反向/稳定扩散。
- **Stable Diffusion**：在隐空间 (latent space) 操作的扩散模型。
- **GAN（生成式对抗网络）/ VAE（变分自编码器）/ Transformer**：三类生成架构。

**成本与生命周期**
- **基于令牌的定价 (Token-based Pricing)**：按输入+输出 Token 计费。
- **FM 生命周期**：数据选择→模型选择→预训练→微调→评估→部署→反馈。

**局限**
- **幻觉 (Hallucination)**：编造不实信息。

### ☁️ AWS 服务速查卡（本任务重点）

| 服务 | 一句话 / 何时用 |
|------|-----------------|
| **Amazon Bedrock** | 一个 API 调多家基础模型，构建 GenAI 应用 |
| **Amazon Titan** | Amazon 自家的 FM（文本/图像/音频），Bedrock 中可用 |
| **Amazon Q Developer**（原 CodeWhisperer）| 实时**代码生成/补全**建议 |
| **SageMaker JumpStart** | 预训练模型中心（含 Stable Diffusion），可微调部署 |
| **Amazon Nimble Studio / Sumerian** | 虚拟制作 / 3D 内容创作 |

### 易考点 / 陷阱

- **GenAI 是深度学习的子集**，核心是**创造新内容**（对比普通 AI 的分类/预测）——概念题常考这个区别。
- **FM 生命周期七步**（数据选择→模型选择→预训练→微调→评估→部署→反馈）建议背下来，考试指南明确列出。
- **术语链要理清**：文本 →(分词器)→ Token/输入ID →(嵌入)→ 向量 →(自注意力)→ 理解上下文 →(Softmax)→ 下一个 Token。
- **自注意力的关键词是 Query/Key/Value + 长距离依赖 + 并行**；位置嵌入负责"顺序"。
- **零/单/少样本**：看提示词里给了**几个示例**（0/1/多）；都属于**上下文学习**，不改模型权重。
- **LLM 是单模态**（纯文本）；能处理图像/音视频的才是**多模态**——别混。
- **扩散模型**关键词：**加噪→迭代降噪**、正向/反向/稳定扩散、Stable Diffusion 用**隐空间**；常用于**图像生成**。
- **调优优先级**：先提示词工程/上下文学习 → 再微调 → 再 RLHF（从便宜到贵、从简单到复杂）。
- **幻觉 (Hallucination)** 是 LLM 固有局限（编造信息），仅靠训练难完全消除——RAG/事实核查可缓解（领域 3/5）。
- **基于 Token 定价**：输入+输出都算钱，提示越长/输出越长越贵越慢。

### 🎴 闪卡 Q&A（遮住答案自测）

<details><summary>1. 生成式 AI 与普通 AI 的核心区别？它是什么的子集？</summary>
GenAI 侧重<strong>创造新原创内容</strong>（文本/图像/音视频/代码），普通 AI 侧重分类/预测。GenAI 是<strong>深度学习</strong>的子集。</details>

<details><summary>2. 基础模型 (FM) 的特点？</summary>
海量数据预训练、<strong>数十亿参数</strong>的超大神经网络；参数越多内存越大、能力越强；可原样用或微调。</details>

<details><summary>3. 从文本到"理解"，经过哪些环节？</summary>
文本 →(分词器)→ Token/输入ID →(嵌入 embedding)→ 向量 →(自注意力)→ 捕获上下文 →(Softmax)→ 预测下一个 Token。</details>

<details><summary>4. 自注意力用到哪三个向量？解决了什么问题？</summary>
查询 Query、键 Key、值 Value。它能捕获 RNN 难学的<strong>长距离依赖</strong>，并支持并行计算。</details>

<details><summary>5. 零样本、单样本、少样本的区别？属于什么？</summary>
提示词里给的示例数分别是 0 / 1 / 几个；都属于<strong>上下文学习 (in-context learning)</strong>，不改模型权重。</details>

<details><summary>6. 单模态和多模态的区别？LLM 属于哪种？</summary>
单模态只处理一种数据（LLM = 纯文本）；多模态处理图像/音视频等多种。LLM 是<strong>单模态</strong>。</details>

<details><summary>7. 扩散模型怎么工作？三个组成部分？</summary>
从随机噪声出发、<strong>迭代降噪</strong>生成连贯输出。三部分：正向扩散、反向扩散、稳定扩散。Stable Diffusion 在<strong>隐空间</strong>操作。</details>

<details><summary>8. 基础模型 (FM) 生命周期的七个阶段？</summary>
数据选择 → 模型选择 → 预训练 → 微调 → 评估 → 部署 → 反馈。</details>

<details><summary>9. 提升 GenAI 表现的调优手段，应按什么顺序尝试？</summary>
先<strong>提示词工程 + 上下文学习</strong>（零/少样本）→ 不够再<strong>微调</strong> → 再 <strong>RLHF</strong>；全程用评估衡量。（从便宜到贵）</details>

<details><summary>10. LLM 的两个基本局限？</summary>
幻觉（编造信息）、复杂推理与数学能力有限。</details>

### 📝 自测练习题（先做，再点开答案）

> ⭐ 为易错题。

**Q1（单选）** 生成式 AI 最本质的特点是？
A. 对已有数据分类
B. 预测未来数值
C. 生成新的原创内容
D. 只做数据清洗

<details><summary>答案与解析</summary>
<strong>C</strong>。GenAI 是深度学习子集，核心是创造新内容；分类/预测是普通 AI 的侧重点。</details>

**Q2（单选）** 分词器 (tokenizer) 的作用是？
A. 把模型部署到终端节点
B. 把人类文本转换成带 Token ID 的向量
C. 给数据打标签
D. 监控模型漂移

<details><summary>答案与解析</summary>
<strong>B</strong>。分词器把文本切成 Token 并转成输入 ID/向量，每个 ID 对应词汇表中的一个 Token。</details>

**Q3（单选）** ⭐ 在向量空间中，两个词的嵌入向量距离很近，说明？
A. 它们拼写相同
B. 它们语义相近
C. 它们出现频率相同
D. 它们属于不同语言

<details><summary>答案与解析</summary>
<strong>B</strong>。嵌入捕获语义，向量越接近语义越相似。</details>

**Q4（单选）** Transformer 相比 RNN 的关键创新是？
A. 卷积层
B. 自注意力机制（Query/Key/Value）
C. 决策树
D. 数据增强

<details><summary>答案与解析</summary>
<strong>B</strong>。自注意力让模型权衡序列各部分重要性、捕获长距离依赖并并行计算。</details>

**Q5（单选）** 在提示词中给模型提供 3 个示例来说明任务，这属于？
A. 零样本推理
B. 单样本推理
C. 少样本推理
D. 微调

<details><summary>答案与解析</summary>
<strong>C</strong>。给多个（几个）示例 = 少样本 (few-shot)；0 个=零样本，1 个=单样本。都属上下文学习，不改权重。</details>

**Q6（单选）** ⭐ 下列哪个是**单模态**模型的典型例子？
A. 根据文字生成图像的模型
B. 纯文本输入输出的 LLM
C. 能看图并回答问题的模型（VQA）
D. 图像字幕模型

<details><summary>答案与解析</summary>
<strong>B</strong>。LLM 输入输出都是文本，属单模态。A/C/D 都跨文本+图像，是多模态。</details>

**Q7（单选）** 要根据文本描述生成高质量图像，最相关的模型类别是？
A. 逻辑回归
B. 扩散模型（如 Stable Diffusion）
C. 决策树
D. K-means 聚类

<details><summary>答案与解析</summary>
<strong>B</strong>。扩散模型通过迭代降噪生成图像，Stable Diffusion 是文本生图的代表。</details>

**Q8（多选，选 3 项）** 以下哪些是考试指南列出的 FM 生命周期阶段？
A. 数据选择
B. 预训练
C. 微调
D. 编写前端页面

<details><summary>答案与解析</summary>
<strong>A、B、C</strong>。FM 生命周期：数据选择→模型选择→预训练→微调→评估→部署→反馈。D 不属于。</details>

**Q9（单选）** ⭐ 提升 GenAI 应用表现时，通常应**最先**尝试哪种方法（成本最低）？
A. 从头训练一个新模型
B. 提示词工程 / 上下文学习
C. RLHF
D. 扩容 GPU 集群

<details><summary>答案与解析</summary>
<strong>B</strong>。调优优先级：先提示词工程/上下文学习 → 不够再微调 → 再 RLHF。先便宜后贵。</details>

**Q10（单选）** LLM 在不知道答案时"一本正经地编造信息"，这种现象叫？
A. 过拟合
B. 数据漂移
C. 幻觉 (Hallucination)
D. 欠拟合

<details><summary>答案与解析</summary>
<strong>C</strong>。幻觉是 LLM 的固有局限之一；可用 RAG、输出验证等缓解（领域 3/5）。</details>

**Q11（单选）** 关于"基于令牌 (Token) 的定价"，正确的是？
A. 只按输入 Token 收费，输出免费
B. 输入和输出 Token 都计费，提示越长/输出越长越贵
C. 与文本长度无关
D. 只按调用次数收费，与 Token 无关

<details><summary>答案与解析</summary>
<strong>B</strong>。通常输入+输出 Token 分别计价；提示和输出越长，成本越高、延迟越大。</details>

**Q12（单选）** 模型上下文协议 (MCP) 的主要作用是？
A. 压缩模型体积
B. 作为标准协议让智能体连接外部系统/工具/数据源
C. 给图像去噪
D. 计算 ROI

<details><summary>答案与解析</summary>
<strong>B</strong>。MCP 是让 AI 智能体连接外部系统与工具的标准协议（智能体 AI 概念，领域 3 细讲）。</details>

---

## 任务说明 2.2：了解 GenAI 解决业务问题的能力和局限性

**官方目标：**
- 描述 GenAI 的优势（适应性、响应能力、对话能力、生成内容的能力）
- 确定 GenAI 解决方案的缺点（幻觉、可解释性、不准确、不确定性）
- 识别选择 GenAI 模型时需考虑的因素（模型类型、性能要求、性能、限制、合规性、成本、延迟、模型复杂性）
- 确定 GenAI 能应用的业务价值和衡量指标（跨领域表现、ROI、效率、转化率、每用户平均收入 [ARPU]、准确率、客户终身价值 [CLV]）

### 🌱 一句话入门（零基础先看这里）

这个任务回答三件事：**GenAI 好在哪、差在哪、以及怎么挑模型和衡量它值不值**。

- **优势**：适应性强、响应快、上手简单——GenAI 让原本又贵又难的 AI 应用变得**更便宜、更快**就能建出来。
- **局限**：会**幻觉**（自信地编造错误信息）、可能输出**有害内容**、**不记得**上次对话、复杂推理和数学弱。
- **选模型 & 衡量价值**：按模型类型/性能/成本/合规等因素选；用**业务指标**（ROI、转化率、CLTV、准确率等）判断它带来的价值。

> 一个判断 LLM 能不能做某任务的小窍门：**"如果给一个 10 岁小孩同样的提示词（以及需要的背景资料），他能做到吗？"** 能，则 LLM 通常也能。

### 视频学习笔记

> 本任务共 3 节课。

---

> **第 1 课：GenAI 的优势与局限**

#### 1. GenAI 的优势

- **通用技术**：像深度学习一样用途广泛，可用于跨多个经济领域的众多应用，不限于单一场景。
- **适应性、响应能力、简单性 (adaptability, responsiveness, simplicity)**。
- 很多传统 AI 系统**构建复杂、成本高**；GenAI **简化了构建过程**，让企业**更低成本、更快速**地建出有价值的 AI 应用。

#### 2. GenAI 的局限（重点）

- **不是万能的**；了解局限才能建立负责任、合乎道德、公平的模型（领域 4 深入负责任 AI）。
- **无记忆**：每次提示，LLM **并不记得之前的对话**（类比：每次把同一任务派给"不同的小孩"）。想让它懂你的业务细节/写作风格，靠**微调 (fine-tuning)**。
- **判断 LLM 能力的小窍门（"10 岁小孩测试"）**：
  - 只需按提示词说明就能完成的任务（如"读这封邮件，判断是否投诉"）→ LLM 能做。
  - 需要它不具备的**专门知识**（如写一篇关于全新 AWS 服务的文章）→ 单靠模型做不到；但**在提示词里提供相关资料**（博客、新闻稿）后，它就能写出有细节的内容（这正是上下文学习/RAG 的价值）。

---

> **第 2 课：指令微调、有害输出、可解释性、评估指标**

#### 1. 指令微调 (Instruction Fine-tuning)

- 目标：进一步训练模型，使其**更好理解人性化提示词**、生成**更自然、更像人**的响应。
- 比只做预训练的原始版本，性能更可持续、语言更自然。

#### 2. 有害输出与人类价值观

- 因为 LLM 基于**互联网海量文本**训练，可能学到并产生：**有毒语言、攻击性/歧视性回复、危险主题的详细信息、误导或错误答案**。
- **幻觉示例**：问"糖尿病人是不是该以碳水为主"，模型本应反驳，却可能**自信地给出完全错误**的答案。对策：**先向权威来源核实，再以此为依据**。
- **三大人类价值观（HHH）**：**有用性 (Helpfulness)、诚实性 (Honesty)、无害性 (Harmlessness)**——指导负责任用 AI（领域 4 细讲）。
- **RLHF（基于人类反馈的微调）**：让模型更符合人类偏好，提升 HHH、**降低毒性、减少错误信息**。

#### 3. 可解释性/可诠释性 (Interpretability)

- **性能 vs 可解释性的权衡**：模型"预测什么"（性能）与"为什么这么预测"（可解释性）常需取舍。
- 两类方法：
  - **内在分析 (Intrinsic)**：用于**低复杂度/关系简单**的模型；简单关系可能**降低性能**（抓不住复杂非线性关系）。
  - **事后分析 (Post-hoc)**：既能解释简单模型，也能解释**复杂模型（如神经网络）**；通常**与模型无关**，可在**局部 (local，单个数据点)** 或**全局 (global，整体行为)** 层面解释。

#### 4. 评估指标（语言类）

- 传统 ML 输出确定，可算**准确率**；但 LLM 输出**不确定**，语言评估更难（如"我喝咖啡"vs"我不喝咖啡"差别细微），需**自动化、结构化**方法。
- **ROUGE（摘要评估）**：把自动生成的摘要与**人工参考摘要**比较，评估**摘要质量**。
- **BLEU（翻译评估）**：把机器翻译与**人工翻译**比较，评估**翻译质量**。
- （ROUGE/BLEU 在任务 3.4 会继续深入。）

---

> **第 3 课：选择模型的因素 + 业务指标**

#### 1. 选择模型的考量因素

- **按内容类型选**：FM 可生成文本/聊天、图像、代码、视频、嵌入等；可调整算法/结构适配特定领域和任务。
- **常用生成模型**：**VAE（变分自编码器）、GAN（生成式对抗网络）、自回归模型 (Autoregressive)**；各有优缺点，取决于数据复杂度和质量。
- 市场上 FM **数量和规模快速增长**，已有数十种可选。
- **FM 特点**：基于**庞大、未标注、广泛**的数据集训练，比传统 ML 模型**大得多**（传统 ML 多用于更具体功能）；FM 作为**开发的基准起点**。
- **不同 FM 擅长不同领域**：如 Stable Diffusion 擅长图像生成，GPT-4 擅长自然语言生成。

#### 2. 用业务指标衡量价值（重点）

- **业务指标示例**：跨域性能、效率、转化率、每用户平均收入 (ARPU)、准确率、**客户生命周期价值 (CLTV/CLV)**、ROI。
- **输出质量指标**：相关性、准确率、连贯性、适当性 → 影响用户满意度和采用率（尤其面向客户的聊天机器人）。用**预定义标准**衡量。
- **效率指标**：**任务完成率、减少人工工作量** → 提升运营效率；**低错误率**保持准确率与可信度。
- **CLTV 提升策略**（示例）：忠诚度计划、品牌忠诚、收集反馈、交叉销售、个性化体验。
- **跨域性能 (Cross-domain Performance)**：评估知识/技能在不同领域的迁移与应用。
- **落地挑战**：需与现有系统集成（数据库、ERP、CRM）、需有技术人才、需算力和基础设施、要控成本。
- AWS：**Amazon Lookout for Metrics + Amazon Forecast** 可做业务指标分析（预测未来值、检测异常并找根因）。
- 记住：**AI 在发展，要持续测量、监控、审查、重新评估**，确保满足业务目标。

#### 📎 补充资料（额外阅读）：选择基础模型的深入考量

> 来源：AWS "Selecting the right foundation model for your startup" 整理。这些选型因素**也与任务 3.1 高度相关**。

**选择 FM 的关键因素（高频考点）**
- **定制程度 (Level of customization)**：从"改提示词"到"完全重训练"，能多大程度改变输出。
- **模型规模 (Model size)**：参数量，代表学到多少信息。
- **推理选项 (Inference options)**：从自管部署到 API 调用。
- **许可协议 (Licensing)**：有些协议**限制或禁止商业使用**——选型必查。
- **上下文窗口 (Context window)**：单次提示能容纳多少信息。
- **延迟 (Latency)**：生成输出要多久。
- 还有：成本、质量、隐私。

**基准测试 (Benchmarking)**
- **通用基准 (Generalized benchmarks)**：如 Stanford **HELM**（语言模型整体评估）——适合**起步筛选**该试哪些模型。
- **自定义基准 (Custom benchmarking)**：针对**你的具体任务**（如"总结医疗预约"）评估，更靠谱。手段包括算 **BLEU / ROUGE** 分数（量化 AI 文本在人工审核前需要多少修正）。
- 陷阱：容易**对某个测试用例过拟合**，以为选对了模型，一上生产就翻车 → 需要**快速试错的实验流程**。

**小型专用模型 (Smaller, purpose-built models) 崛起**
- "一刀切"的大模型往往不如**为特定垂直领域（如营销）定制**的小模型有效。
- 小型专用模型能**大幅减少参数量**却保持领域任务能力，**算力需求更低、性价比更好**。
- 开源社区推动创新：**Falcon 40B、Alpaca** 等；**Hugging Face Open LLM Leaderboard** 对开源模型排名。
- **PEFT（参数高效微调，Parameter-Efficient Fine-tuning）**：只调整**少量参数**、冻结其余预训练参数，**大幅降低计算和存储成本**；这类深度定制在**纯 API 的闭源 FM 上通常做不到**。
- **护栏 (Guardrails)**（如 NVIDIA NeMo Guardrails）：把模型限制在特定领域，**防止幻觉**（无关/错误/意外输出）。

**推理灵活性 + 可持续性**
- 开源/自管模型可**自定义托管方式**（自动扩缩、冗余保证可靠性；数据留在专属环境满足安全要求）。
- **AWS Graviton3（ARM 芯片）**：跑开源模型推理**成本最多省 ~50%**、**能耗最多低 ~60%**（相比同类 EC2 实例）。
- **可持续性 (Sustainability)**：AWS **Carbon Footprint（碳足迹报告）** 帮助比较不同硬件的能效——选型时的环境考量（也呼应领域 4 负责任 AI）。

### 关键术语速记

> 术语以「中文 (English)」对照。

**优势 / 局限**
- **优势**：适应性 (Adaptability)、响应能力 (Responsiveness)、对话能力、生成内容能力、简单性。
- **幻觉 (Hallucination)**：自信地编造错误信息。
- **无记忆**：LLM 默认不记得上一次对话；靠微调注入业务知识/风格。
- **有害输出**：毒性、攻击性、歧视性内容。

**对齐与微调**
- **指令微调 (Instruction Fine-tuning)**：让模型更懂人类提示、回答更自然。
- **RLHF（基于人类反馈的强化学习）**：对齐人类偏好，提升 HHH、降毒性。
- **HHH：有用 (Helpful) / 诚实 (Honest) / 无害 (Harmless)**。

**可解释性**
- **可诠释性 (Interpretability)**：能否解释"为何这样预测"；与性能权衡。
- **内在分析 (Intrinsic) / 事后分析 (Post-hoc)**；事后分析可**局部 (local) / 全局 (global)**。

**评估指标**
- **准确率 (Accuracy)**：传统 ML 可用；LLM 输出不确定较难直接用。
- **ROUGE**：评估**摘要**（对比人工参考摘要）。
- **BLEU**：评估**翻译**（对比人工翻译）。

**模型类别**
- **VAE / GAN / 自回归模型 (Autoregressive)**：常用生成模型。
- **基础模型 (FM)**：庞大未标注数据训练、作为开发起点。

**业务指标**
- **ROI（投资回报率）、转化率 (Conversion Rate)、ARPU（每用户平均收入）、CLTV/CLV（客户生命周期价值）、跨域性能 (Cross-domain Performance)、任务完成率**。

### ☁️ AWS 服务速查卡（本任务重点）

| 服务 | 一句话 / 何时用 |
|------|-----------------|
| **Amazon Lookout for Metrics** | 自动检测业务指标中的**异常**并找根因 |
| **Amazon Forecast** | 时间序列**预测**业务指标未来值 |
| **Amazon Bedrock** | 选择/调用多家 FM 构建 GenAI 应用（选模型时的主入口）|

### 易考点 / 陷阱

- **"何时用/不用 GenAI"与优势**：GenAI 优势是**降低门槛、降成本、提速**地构建 AI 应用；关键词适应性/响应/简单。
- **四大缺点必记**：**幻觉、可解释性差、不准确、不确定性**；另注意 **LLM 无记忆**（靠微调注入知识/风格）。
- **幻觉的应对**：向**权威来源核实**、RAG 事实依据、输出验证（领域 3/5）。
- **ROUGE = 摘要评估，BLEU = 翻译评估**——这组对应关系高频考，别搞反。
- **准确率对 LLM 不好用**（输出不确定），需要 ROUGE/BLEU/人工评估等（领域 3.4 深入）。
- **可解释性方法**：内在（简单模型）vs 事后（含复杂模型、与模型无关、可局部/全局）。
- **选模型看内容类型 + 数据复杂度/质量**：文本→LLM/GPT；图像→扩散模型/Stable Diffusion。
- **业务价值用业务指标衡量**：ROI、转化率、ARPU、**CLTV**、跨域性能、任务完成率——区分"技术指标"(准确率/ROUGE) 和"业务指标"(ROI/CLTV)。
- **HHH（有用/诚实/无害）** 是负责任 AI 的价值观（领域 4 细讲）。

### 🎴 闪卡 Q&A（遮住答案自测）

<details><summary>1. 用一句话概括 GenAI 相对传统 AI 开发的优势。</summary>
GenAI 简化了 AI 应用的构建，让企业能<strong>更低成本、更快速</strong>地建出有价值的应用（适应性强、响应快、上手简单）。</details>

<details><summary>2. GenAI/LLM 的主要局限有哪些？</summary>
幻觉（编造）、可解释性差、不准确、不确定性；还可能输出有害内容；且<strong>默认不记得上一次对话</strong>；复杂推理和数学弱。</details>

<details><summary>3. LLM 不记得历史对话，想让它懂你的业务知识/写作风格怎么办？</summary>
用<strong>微调 (fine-tuning)</strong>；临时任务也可在提示词里提供资料（上下文学习/RAG）。</details>

<details><summary>4. HHH 指哪三个价值观？靠什么微调技术强化？</summary>
有用 (Helpful)、诚实 (Honest)、无害 (Harmless)；靠 <strong>RLHF</strong>（基于人类反馈的强化学习），还能降毒性、减错误信息。</details>

<details><summary>5. ROUGE 和 BLEU 分别评估什么任务？</summary>
ROUGE 评估<strong>摘要</strong>（对比人工参考摘要）；BLEU 评估<strong>翻译</strong>（对比人工翻译）。</details>

<details><summary>6. 为什么准确率对评估 LLM 不太够用？</summary>
LLM 输出<strong>不确定</strong>、是语言，细微差别（"喝/不喝"）难用简单准确率衡量，需 ROUGE/BLEU/人工评估等结构化方法。</details>

<details><summary>7. 内在分析和事后分析的区别？</summary>
内在分析用于简单/低复杂度模型；事后分析可解释复杂模型（如神经网络），通常与模型无关，可在局部（单点）或全局（整体）层面进行。</details>

<details><summary>8. 举例说明"技术指标"和"业务指标"的区别。</summary>
技术指标：准确率、ROUGE、BLEU；业务指标：ROI、转化率、ARPU、CLTV、任务完成率、跨域性能。</details>

<details><summary>9. 提升客户生命周期价值 (CLTV) 的常见策略？</summary>
忠诚度计划、建立品牌忠诚、收集反馈、交叉销售、个性化体验。</details>

<details><summary>10. AWS 里做业务指标"异常检测"和"预测"分别用什么？</summary>
异常检测用 Amazon Lookout for Metrics；预测用 Amazon Forecast。</details>

### 📝 自测练习题（先做，再点开答案）

> ⭐ 为易错题。

**Q1（单选）** 关于生成式 AI 的优势，下列描述最准确的是？
A. 它能保证输出 100% 准确
B. 它降低了构建 AI 应用的门槛与成本、提升速度
C. 它能永久记住所有历史对话
D. 它不需要任何数据

<details><summary>答案与解析</summary>
<strong>B</strong>。GenAI 简化构建、降本提速；A/C/D 都不成立（会幻觉、默认无记忆、仍需数据）。</details>

**Q2（单选）** ⭐ 一个 LLM 客服助手每开一次新会话就"忘了"之前聊过什么。要让它稳定掌握公司业务知识与写作风格，最合适的做法是？
A. 提高温度参数
B. 微调 (fine-tuning)
C. 换更大的显卡
D. 关闭自注意力

<details><summary>答案与解析</summary>
<strong>B</strong>。LLM 默认无记忆；微调可把业务知识/风格注入模型。临时任务也可用上下文学习/RAG 在提示里给资料。</details>

**Q3（单选）** LLM 自信地给出完全错误的答案，这种现象叫？应对的第一步是？
A. 过拟合；增加数据
B. 幻觉；向权威来源核实
C. 漂移；重新部署
D. 欠拟合；提高复杂度

<details><summary>答案与解析</summary>
<strong>B</strong>。幻觉 (hallucination)；应向权威来源核实答案再采用，也可用 RAG/输出验证缓解。</details>

**Q4（单选）** ROUGE 指标主要用于评估哪类任务？
A. 图像分类
B. 机器翻译
C. 文本摘要
D. 欺诈检测

<details><summary>答案与解析</summary>
<strong>C</strong>。ROUGE 评估摘要质量（对比人工参考摘要）；翻译用 BLEU。</details>

**Q5（单选）** ⭐ 把机器翻译结果与人工翻译对比来打分，用哪个指标？
A. ROUGE
B. BLEU
C. F1
D. AUC

<details><summary>答案与解析</summary>
<strong>B</strong>。BLEU 用于机器翻译评估；ROUGE 用于摘要。</details>

**Q6（单选）** 想让模型输出更符合人类偏好，并减少有害/错误内容，最相关的技术是？
A. 数据增强
B. RLHF（基于人类反馈的强化学习）
C. 批量推理
D. 降维

<details><summary>答案与解析</summary>
<strong>B</strong>。RLHF 对齐人类偏好，提升有用/诚实/无害，降低毒性和错误信息。</details>

**Q7（多选，选 2 项）** 下列哪些属于"业务指标"（而非纯技术指标）？
A. 客户生命周期价值 (CLTV)
B. ROUGE 分数
C. 转化率 (Conversion Rate)
D. BLEU 分数

<details><summary>答案与解析</summary>
<strong>A、C</strong>。CLTV、转化率是业务指标；ROUGE/BLEU 是技术评估指标。</details>

**Q8（单选）** 关于可解释性方法，下列正确的是？
A. 内在分析只能用于神经网络
B. 事后分析可解释复杂模型，且常与模型无关，可局部或全局进行
C. 可解释性越高性能一定越高
D. 复杂模型天然最容易解释

<details><summary>答案与解析</summary>
<strong>B</strong>。事后分析适用于复杂模型、通常模型无关、可局部/全局。内在分析用于简单模型；性能与可解释性通常需权衡。</details>

**Q9（单选）** ⭐ 要选一个模型来做"文本生图"，最合适的模型类别是？
A. 逻辑回归
B. 扩散模型（如 Stable Diffusion）
C. K-means
D. BLEU

<details><summary>答案与解析</summary>
<strong>B</strong>。图像生成用扩散模型；不同 FM 擅长不同领域（GPT 擅长自然语言、Stable Diffusion 擅长图像）。</details>

**Q10（单选）** 要对大量业务数据做异常检测并找根因，AWS 上最合适的服务是？
A. Amazon Lookout for Metrics
B. Amazon Rekognition
C. Amazon Polly
D. Amazon Textract

<details><summary>答案与解析</summary>
<strong>A</strong>。Lookout for Metrics 自动检测业务指标异常并分析根因；预测未来值可配合 Amazon Forecast。</details>

**Q11（多选，选 3 项）** ⭐ 选择基础模型时，下列哪些是应重点评估的因素？
A. 许可协议是否允许商业使用
B. 上下文窗口大小
C. 推理延迟
D. 模型 logo 的颜色

<details><summary>答案与解析</summary>
<strong>A、B、C</strong>。选型因素包括定制程度、模型规模、推理选项、<strong>许可</strong>、<strong>上下文窗口</strong>、<strong>延迟</strong>、成本、隐私等；D 无关。</details>

**Q12（单选）** 想在冻结大部分预训练参数、只调整少量参数的前提下低成本微调开源 LLM，应采用？
A. 从头预训练
B. PEFT（参数高效微调）
C. 数据中毒
D. 批量推理

<details><summary>答案与解析</summary>
<strong>B</strong>。PEFT 只调少量参数、冻结其余，大幅降低计算和存储成本；这类深度定制在纯 API 闭源模型上通常做不到。</details>

**Q13（单选）** ⭐ 一家初创公司想降低开源模型的推理成本并减少能耗（考虑可持续性）。最合适的做法是？
A. 只用最大的 GPU
B. 使用基于 ARM 的 AWS Graviton3 实例
C. 关闭所有监控
D. 增加模型参数量

<details><summary>答案与解析</summary>
<strong>B</strong>。Graviton3 跑开源模型推理最多省约 50% 成本、能耗最多低约 60%；还可用 Carbon Footprint 报告比较能效。</details>

---

## 任务说明 2.3：描述用于构建 GenAI 应用程序的 AWS 基础设施和技术

**官方目标：**
- 确定用于开发 GenAI 应用程序的 AWS 服务和功能（Amazon Bedrock、SageMaker AI、SageMaker JumpStart、Amazon Quick、Kiro、Strands Agents、Amazon Bedrock AgentCore）
- 描述使用 AWS GenAI 服务构建应用的优势（可访问性、较低准入门槛、效率、成本效益、上市速度、满足业务目标的能力）
- 描述 AWS 基础设施对 GenAI 应用的优势（安全性、合规性、责任性、可靠性）
- 描述 AWS GenAI 服务的成本权衡（响应速度、可用性、冗余性、性能、区域覆盖、基于令牌的定价、资源吞吐量、自定义模型）

### 🌱 一句话入门（零基础先看这里）

这个任务回答：**在 AWS 上建 GenAI 应用能用哪些服务、有什么好处、怎么算钱**。

- **为什么用 AWS**：不用从零训练模型（又贵又慢），直接**调现成的基础模型**；门槛低、上手快、成本可控，还自带**安全、合规、可靠**。
- **三层堆栈**：底层（训练/推理的**基础设施与芯片**）→ 中层（**SageMaker** 等 ML 服务，训练/微调模型）→ 顶层（**用 FM 的应用**，如 Bedrock、RAG）。
- **怎么收费**：要么**自己托管**模型（付算力+许可，还要维护）；要么用 **Bedrock 按 Token/按需付费**（省心、可扩展、按用量付钱）——大多数人选后者。

> 核心记忆：**大多数人既不自己训练 LLM、也不自己托管**——直接用 Bedrock 调 FM 最划算。

### 视频学习笔记

> 本任务共 2 节课。

---

> **第 1 课：用 AWS GenAI 服务的优势 + 三层堆栈的安全**

#### 1. 用 AWS GenAI 服务的优势

- **可访问性、较低准入门槛、效率、成本效益、上市速度、达成业务目标的能力**。
- **迁移学习 (Transfer Learning)**：不用从头训练，**用新数据集微调预训练模型**——用**更小的数据集、更少的时间**得到准确模型。预训练模型作为**起点**，算法已懂基础、只需学"如何映射到你的新数据"。
- **SageMaker JumpStart**：按行业最佳实践，提供可快速构建的数据集、模型、算法、解决方案。
- **CAF-AI（AWS 云采用框架-AI）**：AI/ML/GenAI 探索的起点和指南，用于团队内部或与 AWS 伙伴讨论 AI 策略。

#### 2. 数据安全是首要关注

- GenAI 应用最受关注的是**保护敏感业务数据**（个人、合规、运营、财务数据）。
- AWS 首要任务是**安全性和客户工作负载的机密性**。

#### 3. 生成式 AI 三层堆栈（重点）

| 层 | 内容 | 关注点 |
|----|------|--------|
| **底层（基础设施）** | 构建/训练 LLM 与 FM 的工具；训练/推理所需的大量算力、防护机制 | 硬件需求高；用专用芯片降本增效 |
| **中层（ML 服务）** | 访问所有模型 + 构建/扩展 GenAI 应用的工具（如 **SageMaker** 训练/优化 FM）| 开发、部署、迭代 |
| **顶层（应用）** | 用 LLM/FM 写调代码、生成内容、得出见解、采取行动的应用（如 Bedrock、**RAG 应用**）| 面向最终用户 |

#### 4. AWS 专用硬件与 Nitro（性价比 + 安全）

- 用**专用硬件**比传统 CPU/GPU **更好的性价比**（降本）。
- **AWS Nitro System**：专用硬件+固件，强制执行安全限制，**确保任何人都无法访问你在 EC2 上运行的工作负载或数据**。
- 适用于所有基于 Nitro 的实例，包括用 **AWS Inferentia、AWS Trainium**（ML 加速器）的实例，和用 **P4/P5/G5/G6**（GPU）的实例。
- 保护 AI 基础设施 = 未授权者不能访问敏感 AI 数据（如**模型权重**和被处理的数据）。

#### 5. AI 系统安全三组件

- **三个关键组件：输入 (Input)、模型 (Model)、输出 (Output)**——通过安全策略、标准、指南、角色职责来保护。
- **AI 特有漏洞**：**提示词注入 (Prompt Injection)、数据中毒 (Data Poisoning)、模型反演 (Model Inversion)**。
- 相关风险：隐私违例、数据操纵、滥用、决策被破坏 → 用**加密、多重身份验证 (MFA)、持续监控**等应对（领域 5 深入）。

---

> **第 2 课：成本权衡 + 关键 AWS GenAI 服务**

#### 1. LLM 的两种定价模式（高频考点）

| 模式 | 说明 | 特点 |
|------|------|------|
| **自己托管 (Self-hosting)** | 在自己的基础设施上运行 LLM | 需付**算力**，可能还要付 LLM **许可费**；要投资并维护基础设施 |
| **按分词付费 (Token-based)** | 按处理的 **Token 数量**计费 | 每个 Token 是一个离散信息单位（文本的字符/词、图像的像素）；是供应商给 API 调用定价的单位；用 AWS 按 Token 付费**可扩展性更好** |

> 结论：**大多数人不自己训练、也不自己托管**（数据/研究/硬件/存储成本太高）→ 用 Bedrock 按 Token/按需最划算。

#### 2. AWS 全球基础设施与高可用

- 架构组件：**区域 (Regions)、边缘站点 (Edge Locations)、可用区 (Availability Zones)**；提供全球弹性、区域弹性、可用区弹性。
- 许多 **AWS Managed Services (AMS)** 为特定目的构建、**内置高可用**。
- 要理解全球基础设施如何提升**高可用性和容错能力**。

#### 3. 关键 AWS GenAI 服务

- **SageMaker JumpStart**：模型中心，快速部署内置 FM 并集成到应用；提供微调和部署、大量博客/视频/示例 Notebook。微调和部署**需要 GPU**；注意查定价页、**删除不用的终端节点**、遵循成本监控最佳实践。
- **Amazon Bedrock**：托管服务，**通过 API 使用多种 FM**（AWS 策管的 + 第三方如 Cohere、Stability AI）；无需从头建 FM 即可大规模开发 GenAI 应用。
  - 支持**导入自定义权重**、用**按需模式**提供自定义模型；**按用量付费、无长期承诺**。
  - 内置**模型评估**：可对不同 FM 跑推理做实验、按最高准确率调用例；可调**推理参数**得到不同补全。
- **Amazon Titan**：Amazon 自家通用 FM，文本生成的不错选择（很多 FM 用例相似，需按用例选最合适的）。
- **PartyRock**：基于 Bedrock 的平台，用来学基础技术、看 FM 如何响应不同提示词（做播放列表、问答游戏、配方等小应用）。

#### 4. 向量数据库 (Vector Database)

- GenAI 里数据以**嵌入 (embeddings)** 形式存储；嵌入是向量，可**压缩、存储、建索引**做高级搜索。
- 向量数据库是 RAG 等应用的关键（存 FM 的语义表示）。

### ⚠️ 视频未覆盖 / 需补充（对照考纲）

官方目标 2.3 点名的服务里，视频没讲 **Amazon Quick、Kiro、Strands Agents、Amazon Bedrock AgentCore**，补充：

- **Amazon Bedrock AgentCore**：在 Bedrock 上**构建和运行 AI 智能体 (agents)** 的能力/框架——让 FM 能调用工具、访问数据、执行多步骤任务（含身份、内存、网关等）。
- **Strands Agents**：AWS 开源的**智能体开发工具包 (SDK)**，用少量代码构建能推理、用工具的 AI 智能体。
- **Amazon Q**：AWS 生成式 AI 助手（**Q Developer** 写代码 / **Q Business** 企业问答）。
- **Amazon Quick（QuickSight 系列）**：BI/数据分析服务，内置 GenAI（自然语言问数据、自动生成洞察）。
- **Kiro**：AWS 的 **AI 驱动的智能体式开发环境 (IDE)**，支持规格驱动开发。
- 记忆定位：**Bedrock=调 FM 建应用；SageMaker=自建/训练模型；JumpStart=模型中心；AgentCore/Strands=建智能体；Q/Kiro=AI 助手/开发；Quick=BI 分析**。

#### 📎 补充资料（额外阅读）：Bedrock 监控（CloudWatch）+ CAF-AI

> 来源：AWS "Monitoring Bedrock using CloudWatch" / "CAF-AI" 整理。深度监控/安全会在**领域 5** 展开，这里只记与成本/性能相关的要点。

**Bedrock 与 CloudWatch 集成**
- Bedrock **近实时**把指标发到 **Amazon CloudWatch**，可建仪表板、设告警、跨账户观测。
- **关键运行指标（对应成本/性能考量）**：
  - **InputTokenCount / OutputTokenCount**：输入/输出 Token 数 → **对应按 Token 计费**，也帮助决定是否购买预置吞吐量。
  - **InvocationLatency**：调用延迟 → 用 `ModelId` 维度**对比不同模型的延迟**。
  - **InvocationThrottles**：被限流的调用数 → 设告警。
  - Invocations、客户端/服务端错误数、ContentFilteredCount（内容被过滤次数）等。
- **模型调用日志 (Model Invocation Logging)**：可收集所有调用的元数据、请求、响应（文本/图像/嵌入）；**默认关闭，需手动开启**，可发到 S3 / CloudWatch。
- **数据保护 (Data Protection)**：CloudWatch 可用 ML 模式匹配**自动识别并遮蔽敏感数据**（如 100+ 种托管标识符，遮蔽日志里的 IP、PII 等）。

**CAF-AI（AI 云采用框架）补充**
- 是 AWS CAF 的 AI/ML/GenAI 扩展，给出**从概念验证 (POC) 到企业级落地**的成熟度模型和规范指引。
- AI 分层再确认：**AI ⊃ ML ⊃ 深度学习 ⊃ 生成式 AI**（CAF-AI 白皮书的分类图）。
- 与 **Well-Architected ML Lens** 配合使用，指导设计/部署/运营 ML 工作负载。

### 关键术语速记

> 术语以「中文 (English)」对照。

**优势 / 方法**
- **迁移学习 (Transfer Learning)**：用预训练模型 + 小数据集微调，省时省数据。
- **CAF-AI（AI 云采用框架）**：AI 策略探索的起点指南。
- **生成式 AI 三层堆栈**：基础设施层 / ML 服务层 / 应用层。

**基础设施 / 安全**
- **AWS Nitro System**：专用硬件+固件，隔离保护 EC2 工作负载与数据。
- **AWS Inferentia（推理）/ AWS Trainium（训练）**：ML 加速芯片。
- **GPU 实例**：P4/P5/G5/G6。
- **AI 系统三组件**：输入 / 模型 / 输出。
- **AI 漏洞**：提示词注入 (Prompt Injection)、数据中毒 (Data Poisoning)、模型反演 (Model Inversion)。
- **模型权重 (Model Weights)**：需保护的敏感 AI 资产。

**定价 / 基础设施**
- **自己托管 (Self-hosting)**：付算力+许可、要维护。
- **基于分词的定价 (Token-based Pricing)**：按 Token 计费、可扩展。
- **区域 / 可用区 / 边缘站点 (Regions / AZs / Edge Locations)**：高可用与容错。

**关键服务**
- **Amazon Bedrock**：API 调多家 FM、可自定义、按需付费、内置模型评估。
- **SageMaker JumpStart**：模型中心，快速部署/微调 FM（需 GPU）。
- **Amazon Titan**：Amazon 自家通用 FM。
- **PartyRock**：基于 Bedrock 的学习/试玩平台。
- **向量数据库 (Vector Database)**：以嵌入形式存储、索引数据，支撑 RAG。
- **AgentCore / Strands Agents / Amazon Q / Kiro / Amazon Quick**（补考纲）。

### ☁️ AWS 服务速查卡（本任务重点）

| 服务 | 一句话 / 何时用 |
|------|-----------------|
| **Amazon Bedrock** | **首选**：API 调多家 FM 建 GenAI 应用，按需/按 Token 付费 |
| **SageMaker JumpStart** | 模型中心，快速部署/微调 FM（需 GPU）|
| **Amazon Titan** | Amazon 自家通用 FM（文本生成）|
| **PartyRock** | 免费学 GenAI、试提示词的小应用平台 |
| **AWS Trainium / Inferentia** | 训练 / 推理 的专用加速芯片（降本增效）|
| **AWS Nitro System** | 隔离保护 EC2 上的 AI 工作负载与数据 |
| **Bedrock AgentCore / Strands Agents** | 构建 AI 智能体 |
| **Amazon Q / Kiro** | GenAI 助手 / AI 开发环境 |
| **Amazon Quick** | BI 数据分析（内置 GenAI）|

### 易考点 / 陷阱

- **用 AWS 建 GenAI 的优势**关键词：可访问性、低门槛、效率、成本效益、**上市速度 (time to market)**、达成业务目标。
- **三层堆栈**要能对号：基础设施（芯片/算力）↔ ML 服务（SageMaker）↔ 应用（Bedrock/RAG）。
- **两种定价**：自己托管（付算力+许可+维护）vs **按 Token/按需（Bedrock）**；"可扩展、无长期承诺、按用量" → Bedrock。
- **Trainium=训练、Inferentia=推理**——两个芯片别搞反。
- **Nitro** 关键词：**隔离、任何人都无法访问** EC2 工作负载/数据。
- **保护的敏感 AI 资产**包括**模型权重**。
- **AI 三大漏洞**：提示词注入、数据中毒、模型反演（领域 5 会深入）。
- **Bedrock vs SageMaker JumpStart vs SageMaker**：调现成 FM 建应用→Bedrock；模型中心快速部署/微调→JumpStart；从头自建/训练→SageMaker。
- **迁移学习**：用预训练模型 + 小数据微调，省时省钱省数据。
- **嵌入存进向量数据库**支撑高级（语义）搜索，是 RAG 基础。
- **成本最佳实践**：用完**删除 SageMaker 终端节点**、查定价页、监控成本。

### 🎴 闪卡 Q&A（遮住答案自测）

<details><summary>1. 用 AWS GenAI 服务构建应用的主要优势有哪些？</summary>
可访问性、较低准入门槛、效率、成本效益、上市速度、达成业务目标的能力。</details>

<details><summary>2. 什么是迁移学习？好处是什么？</summary>
用新数据集微调预训练模型（而非从头训练），用<strong>更小数据集、更少时间</strong>得到准确模型。</details>

<details><summary>3. 生成式 AI 三层堆栈分别是什么？</summary>
底层基础设施（训练/推理算力与芯片）、中层 ML 服务（如 SageMaker 训练/微调）、顶层应用（用 FM 的应用，如 Bedrock、RAG）。</details>

<details><summary>4. AWS Trainium 和 Inferentia 分别用于什么？</summary>
Trainium 用于<strong>训练</strong>，Inferentia 用于<strong>推理</strong>；都是 ML 加速芯片，性价比优于传统 CPU/GPU。</details>

<details><summary>5. AWS Nitro System 的作用？</summary>
用专用硬件+固件强制安全隔离，确保<strong>任何人都无法访问</strong>你在 EC2 上运行的工作负载和数据（含模型权重）。</details>

<details><summary>6. LLM 的两种定价模式？大多数人怎么选？</summary>
自己托管（付算力+许可+维护）vs 按分词/按需付费（如 Bedrock，可扩展、按用量）。大多数人<strong>不自训不自托管</strong>，用 Bedrock。</details>

<details><summary>7. Amazon Bedrock 是什么？有什么特点？</summary>
托管服务，<strong>通过 API 使用多家 FM</strong>（AWS+第三方），可导入自定义权重、按需付费、内置模型评估，无需从头建 FM。</details>

<details><summary>8. Bedrock、SageMaker JumpStart、SageMaker 怎么区分？</summary>
Bedrock=调现成 FM 建应用；JumpStart=模型中心快速部署/微调；SageMaker=从头自建/训练自定义模型。</details>

<details><summary>9. AI 系统的三个关键组件？三大 AI 漏洞？</summary>
组件：输入、模型、输出。漏洞：提示词注入、数据中毒、模型反演。</details>

<details><summary>10. 嵌入存在哪里以支持语义搜索？</summary>
向量数据库 (Vector Database)——嵌入是向量，可压缩、存储、建索引做高级搜索，是 RAG 的基础。</details>

### 📝 自测练习题（先做，再点开答案）

> ⭐ 为易错题。

**Q1（单选）** 一家初创公司想快速上线一个 GenAI 应用，不想自己训练或维护模型。最合适的做法是？
A. 从头训练一个 LLM
B. 用 Amazon Bedrock 通过 API 调用现成的基础模型
C. 自建数据中心托管开源 LLM
D. 只用 Excel 分析

<details><summary>答案与解析</summary>
<strong>B</strong>。Bedrock 让你按需调用多家 FM，低门槛、快上市、按用量付费，适合不想自训自托管的团队。</details>

**Q2（单选）** ⭐ 关于"基于分词 (Token) 的定价"，正确的是？
A. 只在自己的服务器上才有这种模式
B. 按处理的 Token 数量计费，可扩展性好
C. 与使用量无关，固定月费
D. 只对图像收费

<details><summary>答案与解析</summary>
<strong>B</strong>。按 Token 计费（输入+输出），用 AWS 时可扩展性更好、按用量付费。</details>

**Q3（单选）** 想用更小的数据集和更短时间训练出准确模型，应采用？
A. 从头预训练
B. 迁移学习（微调预训练模型）
C. 数据中毒
D. 关闭 GPU

<details><summary>答案与解析</summary>
<strong>B</strong>。迁移学习以预训练模型为起点，用小数据集微调，省时省数据。</details>

**Q4（单选）** ⭐ AWS 上专门用于**训练**的 ML 加速芯片是？
A. AWS Inferentia
B. AWS Trainium
C. AWS Nitro
D. Amazon Titan

<details><summary>答案与解析</summary>
<strong>B</strong>。Trainium 用于训练，Inferentia 用于推理，别搞反。Nitro 是安全隔离系统，Titan 是 FM。</details>

**Q5（单选）** 要确保任何未授权者都无法访问在 EC2 上运行的 AI 工作负载和模型权重，靠的是？
A. 基于 Token 的定价
B. AWS Nitro System
C. PartyRock
D. ROUGE

<details><summary>答案与解析</summary>
<strong>B</strong>。Nitro System 用专用硬件+固件强制隔离，保护 EC2 工作负载与数据。</details>

**Q6（多选，选 3 项）** 以下哪些是 AI 系统特有的安全漏洞？
A. 提示词注入 (Prompt Injection)
B. 数据中毒 (Data Poisoning)
C. 模型反演 (Model Inversion)
D. 磁盘碎片

<details><summary>答案与解析</summary>
<strong>A、B、C</strong>。提示词注入、数据中毒、模型反演是 AI 特有漏洞；D 与 AI 无关。</details>

**Q7（单选）** 生成式 AI 三层堆栈中，Amazon SageMaker 属于哪一层？
A. 底层基础设施
B. 中层 ML 服务
C. 顶层应用
D. 不属于任何层

<details><summary>答案与解析</summary>
<strong>B</strong>。SageMaker 属中层 ML 服务（训练/优化模型）；底层是算力/芯片，顶层是用 FM 的应用。</details>

**Q8（单选）** ⭐ 想快速从"模型中心"部署一个内置基础模型并微调后投产，最合适的是？
A. SageMaker JumpStart
B. Amazon Polly
C. Amazon Lookout for Metrics
D. AWS Nitro

<details><summary>答案与解析</summary>
<strong>A</strong>。JumpStart 是模型中心，可快速部署/微调 FM（需 GPU）。Bedrock 侧重 API 调用，SageMaker 侧重从头自建。</details>

**Q9（单选）** GenAI 应用中，嵌入 (embeddings) 通常存储在哪里以支持语义搜索？
A. 关系数据库的一张普通表
B. 向量数据库 (Vector Database)
C. S3 Glacier 归档
D. CloudWatch 日志

<details><summary>答案与解析</summary>
<strong>B</strong>。嵌入是向量，存入向量数据库并建索引，支持高级/语义搜索，是 RAG 的基础。</details>

**Q10（单选）** 为优化 SageMaker 上的 GenAI 成本，下列哪项是最佳实践？
A. 永远保留所有终端节点在线
B. 用完后删除不使用的 SageMaker 模型终端节点并监控成本
C. 只用最贵的 GPU
D. 关闭所有日志

<details><summary>答案与解析</summary>
<strong>B</strong>。删除闲置终端节点、查定价页、持续监控成本，是控制 GenAI 费用的最佳实践。</details>

**Q11（单选）** 要监控 Bedrock 的用量以配合"按 Token 计费"做成本分析，最相关的 CloudWatch 指标是？
A. InputTokenCount 和 OutputTokenCount
B. CPUUtilization
C. DiskReadOps
D. NetworkIn

<details><summary>答案与解析</summary>
<strong>A</strong>。Bedrock 向 CloudWatch 发送 InputTokenCount/OutputTokenCount，直接对应按 Token 计费的成本分析；还可用 InvocationLatency 对比模型、InvocationThrottles 设限流告警。</details>

**Q12（单选）** ⭐ 关于 Bedrock 的"模型调用日志 (Model Invocation Logging)"，正确的是？
A. 默认开启，无法关闭
B. 默认关闭，需要手动启用，可发送到 S3 或 CloudWatch
C. 只能记录图像
D. 与安全审计无关

<details><summary>答案与解析</summary>
<strong>B</strong>。调用日志默认关闭、需手动启用，可收集元数据/请求/响应并发到 S3/CloudWatch，用于审计；配合数据保护策略还能遮蔽敏感信息。</details>
