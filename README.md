# LLMs for PMs (and other Knowledge Workers)

As product leaders, we are living in the golden age.

Large Language Models (LLMs) burst onto the scene one year ago with the launch of GPT3.5 / ChatGPT and now, within the last 6 months, we have multiple GPT3.5-class open-weight model LLMs.

As a product leader, an essential tool to the modern PM is LLM skills.  As the number of LLMs evolves, you need to be thinking in multiples - the right LLM for the right job. Think less ChatGPT, more Mistral.  Think local versus cloud, augmented by your internal data.  Both for your products and your productivity. 

Ask yourself: what if you had an AI teammate who with full access to your enterprise data that could:

* Transcribe every meeting
* Summarize every meeting, document, email, slack thread etc.
* Search across your digital work life for most relevant context
* Draft every PRD, blog post, or press release

It would be revolutionary and 10X your impact.  Imagine reclaiming your calendar by having your AI “attend” meetings, capturing full detail at the highest fidelity. 

As a PM, you have access to this AI teammate **today**. As a PM leader, you can multiply the productivity of your team **today**.

PMs need to skill up and get comfortable adding LLMs to your core workflows.  This could mean prompting a local LLM on your Macbook or querying a frontier model via API with a thin layer of python code  (that an LLM can write for you).  Have questions about a command or block of code?  Chat with your LLM to learn & iterate -- learning curves are collapsing as quickly as LLM capabilities accelerate.

Be a LLM PM. 

### LLMs at the Center

I have spent the last decade of my career at leading product teams at enterprise SaaS companies like Salesforce and SAP SuccessFactors.  

IMO, the day-to-day “toolbelt” of a product leader has not changed much in this time -- Google or Microsoft productivity apps along with email and group messaging apps (Slack or Teams);  long-form content (i.e. customer interviews) in Confluence or Notion; analytics in a Tableau-like tool; with the software JTBDs tracked in Atlassian JIRA, Linear, or similar.  However, LLMs have caused me to rethink how product teams get work done moving forward. 

### Why local LLMs?

[Some are declaring the LLM wars “over”](https://www.theinformation.com/articles/the-next-ai-battle-adding-it-to-existing-products?shared=0e405a3210461d84), but for knowledge workers, increasingly powerful LLMs available on your Mac allows a PM to get all the benefits of ChatGPT without having to worry about sharing enterprise IP to other model providers. 

For example, [Mistral](https://mistral.ai/) has released 2 new models in the last three months that outperform the largest Llama 70B model and OpenAI GPT-3.5 that you can run for **FREE** on a recent vintage MacBook at 30 tok/s.  For many (most?) use cases, you can redirect your OpenAI spend.

You can expect the performance improvements to compound as LLMs compete for mindshare and continue to push the performance envelope for edge devices. 

### How do I get started with local LLMs?

[Llamafile](https://github.com/Mozilla-Ocho/llamafile) is the easiest way to run an LLM on your Mac or PC with a single file executable.  Includes support for Mistral 7B, Mixtral and LLaVA multi-modal.  Llamafile author Justine Tunney also wrote a very helpful bash command [blog](https://justine.lol/oneliners/).

[LM Studio](https://lmstudio.ai/) adds a UI with a chat interface with integrated LLM marketplace.

## Key Use Cases

I have been fascinated by the intersection of the emergent capabilities of LLMs and the future of work. What if we pivoted core PM workflows to put a LLM at the center?  For example:

### Transcribe Everything

Post-pandemic, most meetings are now recorded and all meeting vendors offer recording downloads.  Many are adding AI transcription and summarization capability (for additional cost).  

If your organization or vendor does not offer this capability, you can also transcribe every meeting today for free or nominal cost:

**OpenAPI Whisper model**

Apple earlier this month released GPU acceleration support for Whisper for recent vintage M-series MacBooks ([github](https://github.com/ml-explore/mlx)).  Using the Base model, GPU acceleration offered 2X speedup on a 90 minute meeting file (3 mins vs 7 mins transcription time). 

```
import whisper

audio_file = “NovemberBoardMeeting.m4a”
result = whisper.transcribe(model="base", audio=audio_file, fp16=False)
print(result["text"])
```

Transcription time:

<table>
  <tr>
   <td>whisper
   </td>
   <td>Real
   </td>
   <td>User
   </td>
   <td>Sys
   </td>
  </tr>
  <tr>
   <td>Tiny (GPU)
   </td>
   <td>
    <code>2m8.623s</code>
   </td>
   <td>
    <code>1m49.090s</code>
   </td>
   <td>
    <code>0m50.881s</code>
   </td>
  </tr>
  <tr>
   <td>Base (GPU)
   </td>
   <td>
    <code>3m17.200s</code>
   </td>
   <td>
    <code>2m52.650s</code>
   </td>
   <td>
    <code>1m17.005s</code>
   </td>
  </tr>
  <tr>
   <td>Small (GPU)
   </td>
   <td>
    <code>5m25.146s</code>
   </td>
   <td>
    <code>4m55.785s</code>
   </td>
   <td>
    <code>1m55.510s</code>
   </td>
  </tr>
  <tr>
   <td>Base (CPU)
   </td>
   <td>
    <code>5m7.512s</code>
   </td>
   <td>
    <code>6m50.538s</code>
   </td>
   <td>
    <code>2m23.459s</code>
   </td>
  </tr>
</table>

`Apple M2 Max (12‑core CPU, 30‑core GPU, 16‑core Neural Engine), 64GB system memory, 1:33:14 meeting file`

OpenAI also offers a Whisper API endpoint for $0.36/hour. 

**Assembly.AI model**

Assembly.AI offers a paid API service ($0.65/hour) with higher-level abstractions like summarization, actions, speaker identification, and more - which means you can skip the next section. 

### Summarize & Action Everything

Now that you have transcribed everything, LLMs are the essential intelligence layer to summarize and action your meetings. 

Basic prompts with the transcript attached or embedded in the prompt do the trick:

> `Summarize the meeting notes in a single paragraph. Then write a markdown list of the speakers and each of their key points. Finally, list the next steps or action items suggested by the speakers, if any.`  (OpenAI Prompt Engineering [guide](https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions))

Depending on the length of the meeting, you need to think about LLM context windows. Here is a quick rule of thumb:

* Typical size of 30 minute meeting (&lt;8k tokens) - Perfect for Mistral on device
* Typical size of 60 minute meeting (>8k and &lt;16k tokens) - Perfect for Mixtral on device or GPT3.5
* Typical size of 90+ minute meeting (>16k tokens) - GPT4-32k

Here are example commands (if running LLM locally):

> `(echo [INST]Summarize the following text:; links -codepage utf-8 -force-html -width 500 -dump https://justine.lol/oneliners/ | sed 's/   */ /';   echo [/INST]; ) | ./mistral-7b-instruct-v0.1-Q4_K_M-main.llamafile -c 6700 -f /dev/stdin --temp 0 -n 500 --silent-prompt`

> `(echo [INST]Please enumerate any actions from this meeting transcript:; cat 6vn84pv7wq-a7b6-4ff0-9939-ec8e22d16e8b.txt | sed 's/   */ /'; echo [/INST]; ) | ./mixtral-8x7b-instruct-v0.1.Q3_K_M.llamafile -f /dev/stdin --temp 0 -c 20000 --silent-prompt -n 1000`

Note that mistral LLMs require the prompt to be surrounded by `[INST]...[/INST]` text (HuggingFace [docs](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)).
