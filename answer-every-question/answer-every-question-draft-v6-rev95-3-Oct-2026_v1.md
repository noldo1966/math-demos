# Answer Every Question: A Proof Standard for Mathematics Produced with AI

Sep 30, 2026 · @Arnoldo Miranda

Draft v6, revision 95. Draft v5 corrected after independent reviews; Appendix C.3 lists what they found, and the [review record](https://claude.ai/artifact/JTk7pC7YYrEirEm7ueHWb9), published as a separate document, answers the findings of the reviews of Draft v6 and describes the corrections that the reviews of the record led to.

## Abstract

In September 2026, 25 Fields Medalists declared that the goals of artificial intelligence (AI) companies and of the mathematical community are "severely misaligned." I group their complaints under five headings: understanding, the passing of ideas from person to person, attribution, the rush to announce, and the loss of the work that famous problems exist to provoke.

On my reading, three of these complaints describe a result with no one standing behind it: no one who can explain it, teach it or say where it came from. The other two describe a process cut short. I propose a standard that addresses each of the five in part, and I say how far it reaches for each.

The standard has four requirements. A proof states its foundation. It leaves no gap above that foundation. Whoever presents it answers every question about it, at any depth, whatever the question's tone, critique or validity, from their own understanding. And that duty lasts for as long as the result is in use. The requirements are the same whether a person or an AI wrote the proof. They matter most for AI because AI output can arrive in volume, and arrives without the track record that, on my reading of the field's practice (Section 4.3), earns human experts their latitude: the freedom readers give them to skip steps.

I show the standard at work on an elementary geometry problem, where five of seven questions exposed defects in answers whose result was correct from the start; of the other two, one demanded the skipped steps after the AI had already listed the breaks, and one asked for an argument already on the page. I compare the standard with the recommendations published on 29 September 2026 by the Advisory Group on Mathematics and Artificial Intelligence, and with three published responses to the declaration.

This paper was written with an AI system. Appendix C describes how.

## 1. Background

This section gives a reader new to the debate the events, people and terms the paper relies on. Sources are in the References.

### 1.1 What happened

| Date (2026) | Event | Source |
| --- | --- | --- |
| 3 Sept | Terence Tao (University of California, Los Angeles), a signatory of the later declaration, posts a thread on Mathstodon, a social network for mathematicians, about what a hypothetical AI solution of the Navier-Stokes problem would cost the field. On 5 September he adds: "I am not aware of any significant developments in this regard; the above discussion is hypothetical." | Ref. 3 |
| About 7 to 8 Sept | Tristan Buckmaster (New York University) posts a proof that a simplified version of the Navier-Stokes equations can break down, that is, predict impossible behavior such as a fluid reaching infinite velocity. He and Levent Alpöge (an Anthropic employee) had worked on the problem for nearly a year with publicly available models. OpenAI then presents a proof, produced with an internal model, that the full equations can break down, and says it does not intend to claim the Millennium Prize for the problem (Section 1.2). Accusations follow that OpenAI used their work without credit; OpenAI denies it. | Ref. 8 |
| 11 Sept | 25 Fields Medalists post the declaration "A Severe Misalignment of AI in Mathematics." By 16 September it has more than 7,200 signatures. | Refs. 1, 5 |
| By 12 Sept | OpenAI has released a report of ten mathematical results, with Lean formalizations. One of them, credited to its Astra model, is the sphere-packing result discussed in Section 5.6. On 8 September, MIT Technology Review, the magazine of the Massachusetts Institute of Technology (MIT), described Astra as "released just last week." | Refs. 6, 7, 8 |
| 12 Sept | Seewoo Lee publishes two posts working through OpenAI's sphere-packing result and its Lean formalization. | Refs. 6, 7 |
| 17 Sept | Timothy Gowers (Collège de France, Cambridge) explains why he did not sign. | Ref. 4 |
| 18 Sept | The blog Proofs and Prompts publishes responses by Timothy Nguyen and M. Levent Doğan. | Ref. 5 |
| 21 Sept | The Advisory Group on Mathematics and Artificial Intelligence is announced: nine mathematicians, hosted at the Institute for Advanced Study, advising AI companies, with no decision-making power at them. | Ref. 9 |
| 29 Sept | The Advisory Group publishes recommendations on the responsible release of AI-generated mathematics, informed by more than 600 replies from the community. | Ref. 2 |

### 1.2 Terms

- **The Navier-Stokes problem.** The equations of Navier and Stokes describe how fluids such as water and air move. Whether their solutions stay smooth or can break down is one of the seven Millennium Prize Problems set by the Clay Mathematics Institute in 2000.
- **Lean and formalization.** Lean is a proof assistant: a computer program that checks proofs written in a precise formal language. A formalization is a proof written in that language. Lean confirms that the formal proof proves the formal statement. It does not confirm that the formal statement says what the paper's statement says.
- **Sphere packing and the Cohn-Elkies bound.** The sphere-packing problem asks how densely equal spheres can fill space. The Cohn-Elkies bound, found by linear programming, is an upper limit on that density. OpenAI's result concerns how this bound behaves as the dimension grows.
- **Large language model (LLM).** The kind of AI system that produced the results above: a model trained on large amounts of text that generates text in response to a prompt. Astra is the OpenAI model credited with the sphere-packing result. ChatGPT (OpenAI), Claude (Anthropic) and Grok (xAI) are publicly available systems of this kind.
- **Presenter.** Defined in Section 3.

## 2. The complaints

I group the complaints under five headings. Each is given in the declaration's own words (Ref. 1); the last adds Tao's words (Ref. 3).

**Understanding.** "\[S\]olving problems is only a tool and proxy for achieving the primary goal of conceptual understanding and insight. Forgetting this in the world of AI may turn the tool against the primary goal. Indeed, the mass production at faster and faster pace of “true/false” statements could destroy fertile ground instead of breathing life into new ideas."

**Transmission.** "Our ideas we disseminate in talks, private discussions and careful writeups, connecting them to the previous ideas of others. These processes invariably take time and are based on human interaction." And: "without the willing mathematicians who must take care of their development and integration into the mathematical canon, AI-conceived ideas would never become fully alive and the crucial human transmission chain between mathematicians would be lost."

**Attribution.** "As in all creative professions, this raises severe attribution and plagiarism questions."

**The rush.** "Often these solutions are announced in a rush, leaving no time for a proper writeup, the isolation of new methods and ideas, and citing relevant previous work of others."

**The proxy problem.** Famous problems matter for the work they provoke: "Solving one of these problems has been a certain sign of new insights and interesting methods, which would then be studied by a community of mathematicians, through a long and arduous process of talks, discussions, simplifications." Tao, writing on 3 September about a hypothetical AI solution: "In most cases in pure mathematics, the problems are posed not because we desperately want the solution to these problems in and of themselves, but because we have seen from past experience that human-directed efforts to solve these problems tend to spur further development of the field through the efforts to solve such problems, and then to digest any partial or complete solutions that emerge for further insights."

Two more of the declaration's objections belong under this heading. It opens: "the push by AI companies to solve mathematical problems as a benchmark is detrimental to the science of mathematics, and to the mathematical community." Tao's clarification of 5 September ties the benchmark to the proxy problem: the cost lies in "converting a historically productive and motivating problem (such as Navier-Stokes regularity) into a mere viral social media post advertising some benchmark progress." And the declaration widens the concern beyond mathematics: "years of training have traditionally served not only to produce a final answer or product, but also to develop understanding and the ability to formulate new questions and ideas."

### 2.1 What the complaints have in common

None of the five says the results are false. They fall into two groups.

- **Three, as I read them, describe a missing person.** Each names, in its own words, something only a person can supply. Understanding: the declaration sets bare "true/false" statements against "conceptual understanding and insight," and insight is held by someone. Transmission: it names the person outright, "the willing mathematicians who must take care of their development and integration into the mathematical canon." Attribution: "this raises severe attribution and plagiarism questions," and a question needs someone to answer it. On this reading, what is missing in each case is someone standing behind the result who can explain it, teach it and say where it came from.
- **Two, as I read them, describe a process cut short.** The rush is about timing: announcement before the write-up, the isolation of methods and the citations. The proxy problem is about the work that is skipped: in Tao's words, the efforts to solve a problem and to digest its solution, which an announcement of benchmark progress bypasses.

The standard in Section 4 requires the missing person. Section 6 argues that it also restores part of the missing process, and says which part it does not.

The declaration ends: "These issues must be addressed urgently." It proposes no standard. This paper proposes one.

## 3. Definitions

These terms have exactly these senses wherever the paper states the standard or applies it to a proof or a presenter. Where it describes other people's practice or the records in Appendices B and D, the words keep their ordinary meanings: a "reader" is anyone reading, an "answer" can be a solution offered to a problem, and "Step" also names the numbered parts of the figures in Appendices B and D and of the Advisory Group's recommendations. In Appendix A, "Step 0" names a section. In Section 7.4, "foundation" also means a formal proof's axioms and libraries. In Appendix A.10, the heading "The answer" names the value the problem asks for.

| Term | Meaning |
| --- | --- |
| **Reader** | A person who knows the terms, notation and conventions of the field and the results listed in the proof's foundation, and supplies no step. |
| **Foundation** | The list, placed before a proof, of every result the proof uses without proving it. Each is named and, where one exists, given a reference. |
| **Step** | A passage in a proof from one statement to the next. |
| **Gap** | A step the text does not carry out: it asserts, instructs or refers where it should argue. A step that uses a result not listed in the foundation, or a listed result whose hypotheses are not shown to hold, is a gap. "Clearly," "by conjugacy" and "Laplace's principle then gives" are gaps, even when the reader could fill them. |
| **False step** | A false statement in or about a proof: a result invoked wrongly or outside its hypotheses, a source cited for something it does not say, or a false description of the proof itself. A false step is worse than a gap, because it hides that work was done wrongly, and it is always listed separately. |
| **Presenter** | Whoever puts a result forward as established, by publishing or announcing it, and anyone who later takes on the duty to answer for it (Section 4.1, requirement 4). For AI output, the presenter is the person or organization that releases it, never the AI itself. |
| **Question** | Any request for the reason behind anything in a result: a step, a term, the foundation, a cited source, or how the result was produced and where its approach came from. |
| **Answer** | A response that supplies what was asked: the missing step, carried down to the foundation or below it if pressed; the fact asked for, such as a source or a history; or a demonstration, from the foundation, that the question rests on a mistake. |
| **Answered for** | A result is answered for while its presenter stands ready to answer, has answered, or is answering, every question put so far, and understands every answer given. This is a condition that holds over time, not a certificate issued once. |

Two consequences follow from these definitions together with the duty to answer in Section 4.1.

1. **Disagreement between readers can be resolved by answering.** If one reader finds a gap that another does not, the presenter either supplies the step or points to where it is on the page, and every reader can then check the answer.
2. **"Every question" is never a completed list.** A new question can be put at any time. The standard does not ask that all possible questions be answered in advance. It asks that each question be answered when it is put.

The distinction between a gap and a false step is not new. Don Fallis separates an inferential gap, where "the particular sequence of propositions that the mathematician has in mind (as being a proof) is not a proof," from an enthymematic gap, where the mathematician "does not explicitly state the particular sequence of propositions that he has in mind (as being a proof)" (Ref. 12, pages 51 and 54). A false step here is close to his inferential gap, and a gap to his enthymematic gap. He also names a third kind, the untraversed gap, left by anyone who "has not tried to verify directly that each proposition in the sequence of propositions that he has in mind (as being a proof) follows from previous propositions in the sequence by a basic mathematical inference" (pages 56 and 57). His account is descriptive: he shows which gaps mathematicians accept, and writes that he is "not claiming that the Cartesian story fails as a normative account of mathematical justification, but merely that it fails as a descriptive account" (page 47). The Cartesian story is his name for the account, which he traces to Descartes, that to know a proof a mathematician "has to work through all the details of the proof step by step" (pages 46 and 47). This standard is normative. It disagrees with the practice Fallis describes, not with Fallis: requirement 2 allows no gap above the foundation.

A recent audit of reviews of mathematical results that OpenAI announced in 2026 names four outcomes that guide its reading of the reviews, two of which concern incomplete steps. Mikołaj and Krzysztof Sienicki distinguish an "unresolved proof gap," which "concerns a necessary step that has not been justified sufficiently for independent verification," from an "expository omission," "a compressed or missing derivation that can be recovered without changing the claim" (Ref. 23, page 3). As I read them, both are gaps under this standard: in each, the text leaves part of the step to the reader, and requirement 2 allows that in neither case, whether or not the reader could recover the step.

## 4. The standard

### 4.1 The four requirements

1. **State the foundation.** Before the proof, list every result it uses without proving it, and state every definition it relies on.
2. **Leave no gap above the foundation.** Every step is carried out on the page, or cites a listed result by name and shows that its hypotheses hold. A reader of the proof supplies nothing.
3. **Answer every question.** The presenter answers any question about the result, at any depth the questioner asks, down to the foundation and below it if pressed. The duty does not depend on the question:
   - **Tone** changes nothing. An angry "Why?" is owed the same answer as a polite one.
   - **Critique** is answered with the missing step if the critique is right, and by showing why it is wrong if it is not; never with a defense of why the step was left out.
   - **Validity** does not exempt a question. A mistaken question is answered by showing, from the foundation, why it is mistaken.
   - **Understanding.** The presenter answers from their own understanding. Each answer, whoever or whatever drafted it, is one the presenter can check against the proof and its foundation and can explain when asked. Relaying an answer the presenter cannot check does not meet the duty.
4. **Keep answering.** The duty lasts for as long as the result is in use. After publication someone may raise a point no one anticipated, and it is owed an answer like any other. Checking already continues after publication in practice: "The mere use of a result by others works as a checking mechanism" (Ref. 15, page 246). When a presenter can no longer answer, the duty passes to whoever takes it on. A result that no one answers for is no longer answered for.

Requirements 1 and 2 govern the text. Requirements 3 and 4 govern the presenter. Requirement 3 needs the presenter to be named, since no one can put a question to a presenter they cannot identify. How an adopter shows that requirements 3 and 4 are being met, by keeping a public record of questions and answers, is set out in Section 9.1.

### 4.2 Where the standard comes from

The duty to answer is not new. The Advisory Group describes it as an existing norm: authors of important work "regularly give seminars at other institutions and talks at conferences, explaining their new developments and answering questions from colleagues" (Ref. 2). The standard makes that norm a duty, and goes beyond that sentence in four ways: to any depth, to every question whatever its tone, to questions about where a result came from as well as how it is proved, and for as long as the result is in use.

Two earlier documents state norms close to parts of the standard. The Leiden Declaration on Artificial Intelligence and Mathematics, of 2 June 2026, counts among the values of mathematical research that "\[r\]esults are attributable to specific authors who take credit for their discovery and assume responsibility for their correctness," and recommends, "\[w\]here a satisfactory attribution is not possible," that authors "state this explicitly in the publication" (Ref. 21). The AI-Generated Science (AIGS) standard of 9 August 2026, which governs an open archive of scientific work to which AI has made a substantive contribution, in mathematics and other fields, and of records that evaluate, correct or challenge such work (Ref. 22, pages 3 to 5 and 8), describes a chain through which a result may pass, from independent review through challenge, response and correction to replication and verification (page 3), and says that "\[s\]ubstantive corrections should be visible rather than silently replacing the historical record" (page 11). As I read them, neither makes answering the duty of a named presenter. The Leiden Declaration, where automated techniques are employed in published mathematical research, places responsibility for "the correctness and adequacy of the arguments and results," and for the citations of prior work, "exclusively with the human authors," and says that mathematicians in general "have a responsibility to" engage in public discourse "to explain and contextualize" methods and results assisted by AI. The AIGS standard's template recommends naming the human submitters responsible for the deposit (page 12), and the standard holds them "responsible for the accuracy of metadata, the characterization of AI contributions, legal and copyright compliance, disclosure of material limitations, and claims made about verification status" (page 6); it says that those whose work is examined "are encouraged to submit responses or corrections" (page 9). This paper's standard makes answering the presenter's duty, for every question, at any depth, for as long as the result is in use.

The idea that a proof answers questions is not new either. Erik Krabbe describes proofs that leave "much room for questioning (or work for the reader, if the author is not there to answer questions)," and others that, "by answering these questions, are developed to great dialectical depth" (Ref. 13, page 464). An earlier proposal of his required that "all the possible dialectic options for that person must be followed through" (page 456). Catarina Dutilh Novaes treats a proof as a dialogue between a Prover and a Skeptic who asks "for clarifications when a particular inferential step by Prover is not sufficiently compelling and perspicuous" (Ref. 14, page 2618).

The standard differs from these accounts in five ways. First, both make a proof's adequacy depend on its audience: proofs succeed "depending upon context and audience" (Ref. 13, page 464), and a proof must be "sufficiently detailed for the intended audience" (Ref. 14, page 2620). The standard fixes the reader as one who supplies nothing above the stated foundation. Second, Dutilh Novaes's Skeptic is a "fair" opponent, and in written proofs "has been internalized by the method itself, and thus silenced" (pages 2617 and 2620). Here the questioners are real people, and every question is owed an answer whatever its tone or validity. Third, Krabbe allows that the author may not be there to answer; here the presenter must be, for as long as the result is in use. Fourth, neither account covers questions about where a result came from. Fifth, neither uses the duty to answer as a condition for releasing results produced with AI.

### 4.3 The same standard for everyone

The requirements are the same whoever or whatever wrote the proof. They bind whoever presents the result. A proof written by a person and a proof produced by a machine meet the same four requirements, and in both cases the question of how the result was produced is owed an answer.

Experts are not exempt. In practice mathematicians accept some gaps. Fallis finds it accepted when a mathematician "(based on his expertise and experience) can 'see that' the details can be filled in" (Ref. 12, page 60). Line Edslev Andersen's interviews with referees find that "\[r\]elatively many gaps are allowed" in standard moves and in the parts of a proof a referee can see "fit right into the literature" (Ref. 15, page 245). That latitude is a convention of the field, not a part of the standard. I propose that it rests on the same duty: when a reader asks, the expert must be able to answer. The sources describe which gaps are accepted; the claim that the latitude depends on this duty is mine. An expert's skipped step is a gap under requirement 2 like anyone else's. On this reading, the latitude consists of readers choosing not to ask yet. Andersen reports a human case: Shinichi Mochizuki's proposed proof of the abc conjecture, a conjecture in number theory, had not been accepted when she wrote, and its author is "rather unwilling to explain his thinking" (Ref. 16, page 2077).

The standard matters most for AI for two reasons, neither of which changes the standard itself.

- **AI output arrives without a track record.** The declaration dates the mathematical abilities at issue to "the last few months" (Ref. 1). So no presenter can yet have a record, built over years, of answering for AI-produced proofs of this kind, and, on the reading above, the convention that grants experts latitude has no such record to rest on.
- **AI output can arrive in volume.** OpenAI released ten results in a single report (Ref. 7), and the declaration warns of "the mass production at faster and faster pace of 'true/false' statements." Output can arrive faster than readers can fill in skipped steps.

So, under the field's convention as I read it, AI output gets no latitude. That is not a stricter rule for AI; it is the same convention without the credit that a record of answering earns. Under the standard itself, no one gets latitude.

## 5. The standard at work

This section reports one case in full and two more briefly. One case cannot establish a general law. It shows what the standard demands in practice and what that demand produced.

### 5.1 The problem

On 30 September 2026 I gave Claude, an AI system made by Anthropic, a geometry puzzle, as an image, and asked for a methodical solution. Here it is stated in full, with the facts shown only in its drawing written out:

> A large circle with center O and radius r touches a straight line at exactly one point, T. A is the point of the circle opposite T, so that O lies between A and T. A smaller circle touches the large circle at B and touches the line at C. A, B and C lie on one straight line, with B between A and C, AB = 14 cm and BC = 6 cm. Find r.

The figure in Appendix A shows the configuration. It illustrates; no step of the proof depends on it.

### 5.2 The first answer

The first answer was correct: r = √70 cm, about 8.37 cm. It argued that triangles ABT and ATC are similar, so that AT² = AB × AC = 14 × 20 = 280, and AT = 2r. It came as an interactive figure with a setup, three steps and an "independent check." Appendix B gives its text as it was shown, and Appendix D gives the whole exchange that followed.

### 5.3 Seven questions

I then questioned the answer. Each question below is quoted as I typed it; where I used strong language, or where the quotation stops before my message did, the omitted words are marked "...". The full exchange is in Appendix D.

| # | The question | What it exposed | What the answer had to add |
| --- | --- | --- | --- |
| 1 | "You didn't explain the key relationship! Why?" | A gap: the caption "So they are similar, and their sides are in the same ratio" gave no correspondence of vertices, and the table wrote △ABT \~ △ATC without any reason why AB pairs with AT. A second gap: the "independent check" rested on the tangent-secant rule, which it cited without proof. The reply also listed two more breaks, the compressed Step 1 and the unargued "AT ⟂ line," which the 07:25 rebuild dealt with. | The matching A to A, B to T, T to C, and the sides it pairs; the check was dropped (07:25) |
| 2 | "Redo the whole thing! ... You skip steps! Do it right!" | Nothing new. It demanded the skipped steps, after Claude had itself listed the breaks at 07:23 (Appendix D). | The rebuild: every step shown with its statement and its reason, though still behind navigation buttons (07:25) |
| 3 | "Why is ∠ABT = 90º? This is not explained!!!!" | No new defect. The argument was already on the page, split across Steps 1 and 2 of the 07:25 figure. | The argument gathered in one place, and the result named as Thales' theorem |
| 4 | "Why didn't you note this!!!!! At the beginning!!!! ..." | The reader had no plan: the key results the proof rests on appeared only when they were reached. | A plan naming the key facts before any work, and every step visible on one page |
| 5 | "Why isn't Thales theorem mentioned?" | The theorem was named in the plan, but not where it was proved and used. | The theorem stated before its proof and named at each use |
| 6 | "Did we prove Thales' theorem?" | The proof needed B ≠ A and B ≠ T without saying so, and used three standard results without listing them: the base angles of an isosceles triangle, the angle sum of a triangle, and angle addition. | The cases argued, and the results named |
| 7 | "... You selectively choose what you want to state and not prove ..." | There was no stated foundation, so the choice of what to prove and what to assume was inconsistent. | A stated foundation, with every other step proved: the proof that became Appendix A |

### 5.4 What this case shows

- **Five of the seven questions exposed a real defect in work presented as finished.** Questions 1 and 4 to 7 did. Question 2 demanded the skipped steps, after the AI had listed the breaks itself. Question 3 asked for an argument that was already on the page, split across two steps; answering it gathered the argument in one place and named it. Requirement 3 applies there too: a question is owed an answer even when what it asks for is already on the page. The first answer's conclusion was right, and its main argument was true. What it lacked was the reasons a reader needs to pass from one step to the next.
- **No question changed the number.** r = √70 throughout.
- **The questions were not all polite, and not all valid.** Two were partly mistaken. Question 3 said the right angle was "not explained," but the argument was on the page, split across two steps. Question 5 asked why Thales' theorem was not mentioned, but it was named once, in the plan; answering it still exposed a real defect, since the theorem was not named where it was proved and used.
- **The questioning led to a proof that states its foundation.** The first answer used the angle sum of a triangle and similar triangles, which Euclid proves from his fifth postulate, without saying so. The final proof lists what it assumes. Appendix A.11, completed during the writing of this paper, says which items of that foundation Euclid proves from the fifth postulate or from results that depend on it: A9, used by the angle-sum lemma L2, on which L3 (Thales' theorem), L5 and L6 depend; and A11, the intercept theorem, used in L6. A10 is assumed, and the paper does not show whether it depends on the postulate. Section A.12, which shows that the configuration exists, uses coordinates (A12), which are assumed to satisfy A1 to A11. The final proof also reduced the one proportion the problem needs to A11, in place of the general theory of similar triangles.

### 5.5 A second case: the tilted squares

Three days earlier the same process ran on another puzzle. Two squares of side 6 overlap, with a corner of one at the center of the other; the second square can be turned about that corner, and the shared area is 9 square units at every angle. The two sides of the second square that meet at that corner are perpendicular and start at the center of the first square; the lines along them cut the first square into four pieces, and the shared area is the piece that lies between the two sides.

- The first explanation used symmetry: turning the picture a quarter turn about the center. I rejected it because it asked the reader to see the four pieces, into which the lines along the two sides of the second square cut the first, as equal in a drawing that was not drawn accurately. It was replaced by a calculation from stated facts.
- While building an interactive version, the AI found that one step of its own argument was circular: it used the equality of two angles to compute the equality it was meant to prove. The order of the argument was corrected before publication.
- The explanation never said why the size of the second square matters. It matters because the second square must cover the part of the first square that lies between its two sides. Every point of the first square is within 3√2 ≈ 4.24 of its center, since its farthest points are its corners. A point of that part, measured from the corner of the second square along its two sides, has both coordinates between 0 and 3√2, which is less than 6, so it lies in the second square. So the second square always covers that part. With side 2, the whole second square lies inside the first, since its farthest corner is 2√2 ≈ 2.83 from the center and every side of the first square is 3 from it; the shared area is then 4, not 9. The final version states this, and is published as an interactive page (Ref. 11).

### 5.6 A case from the field: the sphere-packing report

Seewoo Lee worked through OpenAI's sphere-packing result and its Lean formalization, and published what he found (Refs. 6, 7). His posts show the questioning half of the process, carried out by a reader. They describe no exchange with OpenAI.

- **He questioned an AI to understand the proof,** using Codex, OpenAI's coding assistant: "I had a conversation with ChatGPT in the Codex app where I mostly asked questions about the intuition and choice of parameters in the proof."
- **He wrote the missing exposition himself:** "I have mostly focused on understanding the intuition behind the proof and making it more readable ... Some proofs are expanded with more details."
- **He checked the formalization against the report** and concluded that it "is incomplete," then set out, with an AI, to rebuild it, formalize the missing results and add explanatory comments.
- **He carried the cost.** He upgraded his own AI subscription "for this project."
- **A central question stayed open:** "I still don't understand how the lower and upper bound exponents match, which seems to be the most interesting point." The exponents are the lower and upper bounds on how fast the Cohn-Elkies bound shrinks as the dimension grows; one of the report's two main results is that they agree. Ref. 6 describes that result as "the exact asymptotic rate of the optimal Cohn-Elkies linear program."

By Lee's account, he expanded steps of the report himself. He put his questions to an AI, and wrote the added detail himself. On my reading, his work shows what the standard asks of a presenter by showing who did that work instead, and what remained undone.

## 6. How the standard addresses each complaint

Where a row relies on the public record of questions and answers, it means the standard adopted as Section 9 describes.

| Complaint | What the standard supplies | How far it reaches |
| --- | --- | --- |
| Understanding | A presenter who has answered, or is answering, every question put so far, at any depth, from their own understanding, and stands ready for the next | In part: someone has answered, or is answering, every question put so far. The community's insight still has to be built |
| Transmission | Answers to every question, kept as a public record where the standard is adopted (Section 9.1) | In part: it adds to discussions and write-ups, and does not replace them |
| Attribution | A foundation that names every result used, and a duty to answer "Where did this come from?" | In part: missing credit becomes a question the presenter must answer, and an unanswered one stands on the record |
| The rush | A text that meets requirements 1 and 2 on the day of release, and a presenter who can be identified (Section 4.1) | In part: the text can be checked at release; readiness to answer shows only over time |
| The proxy problem | The work of digesting a result, on my reading of Tao (Section 6.5) | In part: the digestion Tao names, not the effort to solve |

### 6.1 Understanding

A result that is answered for has a presenter who has answered, or is answering, every question put so far, at any depth asked, who understands every answer given, and who stands ready for the next. On my reading (Section 2.1), that supplies the part of understanding that a bare "true/false" statement lacks: someone who can give the reason for every step. The "conceptual understanding and insight" the declaration asks for still has to be built by others, from those answers.

The standard also bears on the declaration's fear of "mass production." Under the standard, no result may be released without a presenter who will answer for it. The standard sets no limit on the number of releases. A presenter who releases more than they can answer for fails requirement 3. This is a requirement the standard places on presenters, not a limit that enforces itself.

### 6.2 Transmission

The declaration describes transmission as "talks, private discussions and careful writeups." A recorded exchange of questions and answers (Section 9.1, item 4) resembles, on my reading, two of the three: each question is a small discussion, and each recorded answer extends the write-up. It is an addition to those forms, not a replacement for them.

### 6.3 Attribution

The standard catches missing credit in two ways.

1. **Results used.** The foundation must name every result the proof uses without proving it. A result the proof uses but does not list breaks requirement 1, and each step that relies on it is a gap.
2. **Ideas and history.** An idea can shape a proof without being a result the proof cites, and a proof can even reproduce earlier work in full without naming it. Neither shows up as a gap. Both can be caught by requirement 3, when someone asks, because "Where did this come from?" is a question in the sense of Section 3, and it must be answered.

The two cases in the news show the second way.

- **Navier-Stokes.** MIT Technology Review reported that Sébastien Bubeck, a member of OpenAI's technical staff, said in a press briefing that the team was inspired to take on the problem after hearing rumors about Buckmaster and Alpöge's efforts. The article itself notes that both proofs use an approach first developed by the mathematicians Diego Córdoba and Luis Martínez-Zoroa. It also reported that Buckmaster asked whether OpenAI's agents had accessed the transcripts of his work with Alpöge, which OpenAI employees denied, and whether OpenAI's models had been trained on those transcripts, which received no response (Ref. 8). That last is a question about how the result was produced. Under the standard it would be owed an answer; as of the article, none had been given.
- **Sphere packing.** Lee identifies the Mellin transform, a standard tool of analysis, as one of the proof's core ideas and notes that it "already appears in Section 5 of the 2016 paper by Cohn and Miller. The report cites CM16 for the radial formulation but does not discuss this particular precedent" (Ref. 6). Here CM16 is Lee's abbreviation for that 2016 paper, and the radial formulation restricts the problem to functions that depend only on distance from the origin. A reader who asks where the Mellin transform idea came from is owed that precedent.

Gowers, who declined to sign the declaration, thinks missing citations are easy to supply: "if you asked an LLM to look at a proof and tell you which ideas in it are close to ideas that are in the literature already, it would be extremely good at that task." Those who have been careless, he writes, "deserve to be criticized." He also calls the problem "a minor matter compared with the survival of mathematics" and expects that "the whole 'credit system' will surely collapse" (Ref. 4). The standard does not depend on credit. I hold that the question "Where did this come from?" is part of understanding a result, whether or not careers still depend on the answer.

### 6.4 The rush

The declaration's complaint is that results are "announced in a rush, leaving no time for a proper writeup, the isolation of new methods and ideas, and citing relevant previous work of others." The standard meets this in two parts.

- **What can be checked at release.** Requirements 1 and 2 apply to the text on the day it is released. A result announced first and written up later fails them on that day, because on that day no proof is on the page, and any reader can check that.
- **What shows only over time.** Whether the presenter will answer questions cannot be checked in advance. The standard makes it visible afterward: the presenter can be identified (Section 4.1), and where the standard is adopted as Section 9 describes, the questions and answers are recorded, so an unanswered question stands against that presenter.

### 6.5 The proxy problem

Tao names two sources of the development that famous problems provoke: "the efforts to solve such problems," and the work "to digest any partial or complete solutions that emerge."

- **Digestion.** I read the questions and answers about a result as part of the work of digesting it; Tao does not define digesting, and this reading is mine. On that reading the standard serves digestion directly, and the record keeps that work for others.
- **The effort to solve.** The standard does not restore this. When a problem is solved quickly, the years of attempts that would have produced new methods do not happen. What the standard offers in its place is partial: on my reading, a reader who questions a result until each step is answered does some of the thinking the solver would have done. Gowers tells of his own early attempts at Fermat's Last Theorem as "an illustration of the phenomenon that was strongly emphasized in this letter signed by 25 Fields medallists, that one learns a lot from thinking about a problem, regardless of whether one solves it" (Ref. 4).

## 7. The Advisory Group's recommendations

The Advisory Group's recommendations of 29 September 2026 (Ref. 2) open by asking AI labs to stop testing advanced problems on proprietary models: "we do not endorse this practice, and we ask them to stop." They then set out two courses for releasing a result.

- **Course 2.A, "Papers that a human understands."** "Papers for which there is a mathematician responsible who fully understands the content should follow the academic mathematical community's traditional norms": a preprint, peer review, and talks.
- **Course 2.B, "Papers that are not yet understood by anybody."** The lab releases the result under a set of technical norms, the numbered items of "Step I," and funds the work needed for people to understand it ("Step II"). Below, "item 1(a)" and so on refer to Step I. That work "must remain organic and community led. It should not be directed by AI labs."

### 7.1 Where the recommendations and the standard agree

| The Advisory Group's item | The standard |
| --- | --- |
| 1(a): scour the literature and cite related ideas "\[e\]ven if the AI lab's model discovered those ideas independently" | The foundation names every result used, and "Where did this come from?" must be answered (Section 6.3) |
| 1(b): "friendly introductions and precise theorem statements and proofs" | Requirement 2. The standard asks more: a proof can state each step precisely and still leave the reason for a step to the reader |
| 2: an independent repository where "subsequent modifications are appropriately recorded," ideally one that "allows for comments on papers" | The public record of questions and answers that adoption adds (Section 9.1, item 4) |
| 2: releases should not be "marketing vehicles" | The rush (Section 6.4) |
| 3: the model, the prompts, a summarized chain of thought (the text a model produces while working toward an answer), the time and the cost | Questions about how the result was produced (Section 3). Here the Group asks more: it requires disclosure at release, while the standard requires an answer when asked. Section 9.1, item 5 adopts the Group's version |
| 4: formalization, or a stated status such as "formalized modulo standard results that are accepted by the community" | A stated foundation (requirement 1), for the formal proof |
| 5: "how exactly AI came to be used on that particular problem," with failures and how problems were chosen | Questions about how the result was produced (Section 3). The Group asks more here too: a record at release. Section 9.1, item 5 adopts a record of how AI came to be used, but not the Group's request for failures and for how problems were chosen |

### 7.2 What the standard adds

1. **A working meaning for "fully understands."** The recommendations turn on whether "there is a mathematician responsible who fully understands the content." Their Background states the norm behind this: authors "should understand the mathematical argument of that paper, have verified its correctness themselves, and take full responsibility for the content." They give no test for it. I propose a test for "fully understands," stated through the Group's own norm of taking full responsibility, and applied over time rather than once: a result belongs in course 2.A while a named presenter answers every question put to it, at any depth, from their own understanding (Section 4.1, requirement 3), and stands ready for the next. The test can show that the condition fails, never that it holds for good: a single question left unanswered shows the condition is not met, and no number of answers completes it (Section 3, consequence 2). A result in course 2.B moves to 2.A when someone who can check the answers takes on that duty and meets it (Section 4.1, requirement 4; Section 8.3); until then it does not meet the standard (Section 8.3).
2. **No gaps, not only precision.** Item 1(b) asks for precise statements and proofs. Requirement 2 asks that the reader supply nothing.
3. **A named presenter.** The recommendations name a responsible mathematician for course 2.A and no mathematician responsible for course 2.B, and they describe answering questions as a norm of the field. The standard makes answering the presenter's duty for every release, for as long as the result is in use.
4. **Comments answered, not only allowed.** Under the standard, each comment that asks a question is owed an answer. Where the standard is adopted as Section 9.1 describes, each answer that changes the text produces a new, recorded version. Joseph Grcar made a similar proposal for journals: they "should be community forums in which new results evolve" (Ref. 18, page 423).

### 7.3 Reaching the standard where AI falls short

The recommendations expect that current models "may not be able to reproduce the level of attribution or quality of exposition that we expect of mathematicians, and thus more important work from mathematicians after release may be needed to reach this standard." They add that this "does not absolve AI labs of the responsibility to do the best they can with their models."

The standard does not depend on what models can do unaided. It asks whether the result, as presented, meets the four requirements. Section 5 shows one way to meet the first three now, for one elementary problem: a person questions, the AI drafts answers, and the person accepts an answer only when the missing step is on the page and the person can check it. Requirement 4 can be shown only over time. In that case the AI did not reach the standard alone, which is consistent with the Advisory Group's doubt.

The failures along the way were part of the work. Three times in the exchange the AI presented work as finished that a question then showed was not: at 07:17, 07:25 and 07:31 (Appendix D). Its last reply, at 07:48, was revised further under questioning during the writing of this paper (Appendix A). Two of my questions, 3 and 5, were partly mistaken (Section 5.4). Each failure was found and answered, and the whole exchange is in Appendix D, so a reader can follow the same path from the first answer to the last.

### 7.4 Formalization

The recommendations ask for formalization "as far as possible." A formal proof checked by Lean shows that its formal statement follows from its formal foundation. It does not show that anyone understands the proof, or that the formal statement is the paper's statement. Checking the second is itself a question in the sense of Section 3, and someone has to answer it.

Lee's comparison shows why this matters (Ref. 7). He found that OpenAI's formalization of the sphere-packing result "is incomplete": half of the report's Theorem 1.2, one of its two main results, is not formalized, and the formal version of the report's Proposition 3.1 "is not equivalent to Proposition 3.1." His diagnosis: "most of the time, people don't read the AI's autoformalized proofs and just believe them." In Fallis's terms, a reader who reads such a proof and accepts it without checking each step leaves an untraversed gap (Ref. 12, pages 56 and 57); a reader who does not read it at all has not traversed even that much, and a gap that no one has checked is what he calls "universally untraversed" (page 47). Autoformalized proofs are proofs that an AI has translated into a formal language such as Lean.

### 7.5 Answering is not directing

The recommendations require that understanding not be "directed by AI labs," and the standard asks for a named presenter. The two are compatible. A presenter answers the community's questions; the community chooses what to ask and judges whether the answers hold.

### 7.6 Access to models

The recommendations ask labs to grant "broad, equitable access to their publicly available models," because "Mathematics advances primarily through collective verification, conceptual synthesis, and shared intuition, none of which can thrive when some instruments generating frontier results are accessible only to a select few."

The standard offers a route to verification and understanding that does not pass through the model: the proof is on the page, and questions about it are answered in public (Section 9.1, item 4). The reader needs no access to the model, because the presenter answers the questions about how the result was produced. A presenter who cannot answer them fails requirement 3. One distinction matters. When a computation is part of a proof, the program is part of the text to be checked, and checking it requires access to it. Kenny Easwaran makes the same point: "If the author provides the code for the relevant computer program, then the reader can presumably see just as well as the author that it does what is claimed" (Ref. 17, page 356). Fallis's example is the four-color theorem, where "large parts of the proof had to be checked using a computer" (Ref. 12, page 58). When a proof stands on the page, what produced it is not part of the text. In Easwaran's terms such a proof is "transferable": an expert can be convinced "just by consideration of each of the steps in the proof," without "a knowledge of the process by which the proof was generated" (Ref. 17, page 343).

The recommendations also warn that unequal access lets well-funded labs "outrun the rest of the field." That concerns who can make discoveries, not whether a discovery can be checked and understood, and the standard does not address it.

## 8. Three responses to the declaration

### 8.1 Timothy Nguyen

Nguyen, a mathematician and AI researcher at Google DeepMind, argues that the Fields Medalists' objections "will not age well" (Ref. 5). Mathematicians already build on results they have not mastered, "routinely invoking theorems they haven't fully digested," and "expertise is not exhaustive; it is selective. So that building upon formally verified machine-generated proofs is an expansion of the mathematical toolkit, not a diminishment of it." He adds: "Understanding is also, in some sense, a luxury."

- **Building on undigested theorems.** The standard does not require every reader to absorb everything. It requires that someone can answer for each result. A community can build on a theorem that few of its members have digested, provided that someone answers for it. I read Nguyen's first point as describing that situation. The standard names the condition it depends on: when a mathematician invokes a theorem they have not digested and it fails them, their recourse is someone who can answer for it.
- **Formally verified proofs.** Building on a formally verified proof is sound when its formal statement is the statement being used. Whether it is, is a question someone must answer, and Section 7.4 shows a case where the answer was no for part of a result.
- **Understanding as a luxury.** Even a reader who values true statements over understanding needs to know which statement was proved, from what, and whether it is the one claimed. Those are questions, and the standard asks only that they be answered.

### 8.2 M. Levent Doğan

Doğan, a different person from Levent Alpöge of Section 1.1 and a postdoctoral researcher at Ludwig Maximilian University of Munich (LMU), argues that the declaration should have used its signatories' influence to change institutions: "I believe that the community leaders should urgently propose standards for papers and publications" (Ref. 5). The standard proposed here is such a standard. An editor, a referee or an advisory body can adopt it without waiting for anyone else.

Doğan also asks: "Why should we assume that AI will become extremely good at proving theorems while remaining fundamentally incapable of explaining them?" The standard assumes neither. It tests the presenter's explanations, by asking questions, whatever models turn out to be able to do.

### 8.3 Timothy Gowers

Gowers, a member of the Advisory Group (Ref. 9), explained why he did not sign the declaration (Ref. 4).

- **Two temperaments.** He does not accept that problem-solving is only a proxy for understanding. Mathematicians sit on "a spectrum" between those driven by solving problems and those driven by understanding, and he does not want to suggest to many of them "that their mathematical temperament is somehow “wrong”." The standard does not rank the two. A problem-solver who presents a result owes the same answers as anyone else, and those answers are what let others check the result and build on it.
- **The use of deep involvement.** He asks: "I would be interested to know what use that level of deep involvement with a proof might have in a world where AI is much better than we are at finding proofs." I propose one use. Whoever takes on the duty to answer owns every answer given, whoever or whatever drafted it (Section 4.1, requirement 3; Section 9.4). Deep involvement with the proof is what lets a person check those answers rather than relay them. In the terms of Section 7.2, a result moves from course 2.B to course 2.A only when someone who can check the answers takes on the duty.
- **Write-ups.** He calls the poor write-ups of AI proofs "almost certainly a temporary annoyance." That is a prediction. The standard does not depend on it: it applies to write-ups as they are.
- **Too much to digest.** He argues that if AI produces more than can be digested, "we could choose which parts of it we wanted to digest." The standard is compatible with choosing. What it does not allow is a release whose presenter cannot answer for it, and the Advisory Group's course 2.B, for "Papers that are not yet understood by anybody," provides for exactly such releases. On this point the standard asks more than the Group: a result released in course 2.B does not meet the standard, and it is not answered for until someone takes on the duty to answer (Section 4.1, requirement 4).

## 9. What adopting the standard requires

Each party that handles AI-produced mathematics can adopt its part without waiting for the others.

### 9.1 Producers of AI mathematics

A result released by an AI producer should come with five things.

1. **A foundation list:** every result the proof uses without proving it, by name, with a reference where one exists, and every definition it relies on. The Advisory Group's items 1(a) and 4 ask for parts of this.
2. **A text with no gaps:** every step above the foundation carried out on the page. This is a stronger form of the Advisory Group's item 1(b).
3. **A named presenter:** a person or organization that accepts the duty to answer questions about the result, at any depth, from their own understanding, for as long as it is in use. The recommendations name a responsible mathematician only for course 2.A; for course 2.B they name no mathematician responsible. This item requires one for every release.
4. **A public record of questions and answers,** kept with the result. When an answer changes the text, the text gets a new version number and the record says why. The Advisory Group's item 2 asks for a repository that records changes, ideally one that allows comments. The sphere-packing release shows the need: its code history was "repeatedly force-pushed," that is, overwritten, "so earlier versions may not be recoverable from its public Git history" (Ref. 7); Git is software that records the history of changes to files. Without a record, a reader cannot tell which version an answer refers to. The proposal has precedents. Grcar found that, across fields, many substantive errors are found through reader comments, "which are especially rare in mathematics" (Ref. 18, page 419). Joachim Frans and Laszlo Kosolosky proposed online databases, and a practice in which "the back-checking, completing, changing, correcting, etc. of proofs are much more highlighted" (Ref. 19, page 358). The AIGS standard sets out a related record for work to which AI has made a substantive contribution, with status labels that include "CHALLENGED" and "CORRECTED" (Ref. 22, page 8), and the Sienickis hold, of reviews, that "\[a\] withdrawn objection should remain documented with the reason for withdrawal" (Ref. 23, page 8). This item places the record of questions and answers with the producer of the result.
5. **A statement of where the approach came from and how the result was produced:** earlier work, conversations or reports that shaped the attempt, whether or not any step depends on them; the name of the model, the prompts used, a summarized chain of thought, the time taken and the estimated cost of computation; and how AI came to be used on the problem. The Advisory Group's items 1(a), 3 and 5 ask for these.

### 9.2 Journals, referees and advisory bodies

- A referee may ask any question about the result. A question the authors leave unanswered is a reason to reject.
- An editor can require items 1 to 5 above as conditions of review for any submission.
- The Advisory Group's recommendations already ask for parts of items 1 to 5; for item 3, they name a responsible mathematician for course 2.A only. The Group could require item 3, a named presenter, for every release, and use the working meaning of "fully understands" in Section 7.2 as the condition for moving a result from course 2.B to course 2.A.

### 9.3 Teaching

The process is also a way to learn. A student given a proof, from a person or an AI, can question it until every step is answered, and keep a record of the questions and answers. The student does the questioning; whoever gives the proof, a teacher or an AI, answers the questions.

Gowers describes a related exchange from the reader's side (Ref. 4). He advises students to read "actively" rather than "passively," and expects that "an LLM could get to know what our mathematical background is and feed us with just the right hints to allow us to work our way through a mathematics paper in this active way."

### 9.4 People working with AI

Anyone who publishes mathematics produced with AI is its presenter and carries the duty. In practice this divides the work.

- The person sets the standard, asks the questions, and decides what is accepted, and understands every answer given in their name.
- The AI drafts, derives and answers, and must say plainly what is proved, what is assumed, and what it has not done.
- Nothing is published until the person is prepared to answer for it, with or without the AI.

Appendix C describes how this worked, and where it failed, in the writing of this paper.

## 10. Conclusion

Mathematicians differ on whether results or the understanding behind them matter most. The Fields Medalists put understanding first, and Gowers places mathematicians on a spectrum between the two. The standard does not need to settle that. Whichever one values, I hold that a result can be checked, taught and built on when someone answers for it, and, on the reading in Section 2.1, three of the declaration's five complaints describe results that arrive with no one doing so.

The remedy proposed here does not depend on knowing who or what wrote a proof, and it does not ask that AI be slowed; it asks that each release have someone answering for it (Section 6.1). It asks four things of every proof and of whoever presents it:

1. State what you assume.
2. Prove everything above it.
3. Answer every question, at any depth, whatever its tone, critique or validity, from your own understanding.
4. Keep answering for as long as the result is in use.

The standard is the same for everyone. It changes practice most for AI, because AI output can arrive in volume, and arrives without the record of answering that, under the field's convention as I read it, earns experts their latitude (Section 4.3).

Gowers declined to sign the declaration partly because he was not sure "what it was demanding that isn't happening already" (Ref. 4). This paper makes a specific demand: those four requirements, of every presenter, from the day a result is released.

## Appendix A. The complete proof

This is the proof the seven questions of Section 5.3 led to, completed during the writing of this paper. Every step either is carried out here or cites an item of the foundation, a definition or an earlier lemma by name. The items of the foundation, the definitions and the lemmas L1, L2, L3 and L5 are general: their letters stand for any points that meet the stated conditions. L4 and L6 are proved for the configuration of A.2 and Step 0.

&#91;embedded content: Figure 1 · the configuration, drawn to scale\]

Figure 1 illustrates the configuration. No step depends on it.

### A.1 Foundation: results assumed, not proved here

1. **A1. Numbers.** Lengths and angle measures are real numbers, with the usual arithmetic. Every positive real number has exactly one positive square root.
2. **A2. Lines.** Through two distinct points there is exactly one line (Hilbert, axioms I.1 and I.2; Ref. 20).
3. **A3. Order.** (a) Of three distinct points on a line, exactly one lies between the other two. (b) A line separates the points not on it into two sides; two such points are on opposite sides exactly when the segment joining them meets the line. (c) If O lies between A and T, and B is not on line AT, then ray BO lies inside angle ABT. (d) If O lies between A and T, then ray AO is ray AT. (e) If B lies between A and C, then A, B, C are distinct points of one line, and B lies between C and A. Items (a) to (e) are Hilbert's axioms of order or follow from them (Hilbert, Chapter I, sections 3 and 4; Ref. 20).
4. **A4. Length.** The distance from a point to itself is 0, and the distance between distinct points is positive. The distance from A to B equals the distance from B to A. If B lies between A and C, then AC = AB + BC. On a ray from a point P there is exactly one point at each positive distance from P. On a line through P there are exactly two points at each positive distance from P, and P lies between them.
5. **A5. Angles.** Every angle has a measure strictly between 0° and 180°. (a) If a ray lies inside an angle, the two angles it forms add to the whole angle. (b) If F lies between T and T′ and O is not on line TT′, then ∠OFT + ∠OFT′ = 180°. (c) Two distinct lines are perpendicular when they meet at a right angle, which measures 90°. Each of the four angles they form at their meeting point then measures 90°.
6. **A6. Side-angle-side.** If two triangles, or one triangle with its corners read in two orders, have two sides and the angle between them equal, they are congruent: all their corresponding sides and angles are equal. (Euclid, Elements I.4; Ref. 10.)
7. **A7. Perpendicular.** From a point not on a line, a perpendicular to the line can be drawn; it meets the line at one point, its foot.
8. **A8. Parallels.** Two lines are parallel when they do not meet. Through a point not on a line there is a line parallel to it (Euclid constructs one in Elements I.31; Ref. 10).
9. **A9. Alternate angles.** If a line crosses two parallel lines at P and Q, and R and S lie on the two parallels on opposite sides of line PQ, then ∠RPQ = ∠SQP. Euclid proves this from his fifth postulate (Elements I.29; Ref. 10); here it is assumed directly.
10. **A10. Angles at a point on a parallel.** Let P, Q, R form a triangle, and let m be a line through P parallel to QR. Let M and N be points of m with P between them, M on the opposite side of line PQ from R. Then ∠MPQ + ∠QPR + ∠RPN = 180°, and N and Q lie on opposite sides of line PR. It is assumed, not derived here.
11. **A11. Intercept theorem.** If D and T lie on one ray from A, E and C lie on another ray from A, the two rays are not on one line, and lines DE and TC are parallel, then AD/AT = AE/AC. Euclid proves it using areas and his theory of proportion (Elements VI.1 and VI.2, with Book V; Ref. 10). Not included.
12. **A12. Coordinates.** Used only in A.12. Points can be labeled by pairs (x, y) of real numbers so that the distance between (x₁, y₁) and (x₂, y₂) is √((x₁ − x₂)² + (y₁ − y₂)²), where √0 means 0; each line is the set of points satisfying an equation ax + by = k, with a and b not both 0; and B lies between A and C exactly when B = A + t(C − A) for some t with 0 < t < 1. Angles are measured in the usual way: the measure of ∠XYZ is the angle between 0° and 180° whose cosine is ((X − Y) · (Z − Y))/(XY × ZY). That this ratio lies strictly between −1 and 1 when X, Y and Z are not on one line, that the cosine takes each such value exactly once between 0° and 180°, and that these coordinates and this measure satisfy A1 to A11 are assumed, not proved here.

**Definitions.** For distinct points A and B, the *segment* AB consists of A, B and the points between them, and the *ray* from A through B, called ray AB, consists of A and every point P of line AB such that A does not lie between P and B. For points X, Y, Z not on one line, the *angle* ∠XYZ is formed by ray YX and ray YZ, and depends only on those two rays. A ray YP *lies inside* ∠XYZ when P and X are on the same side of line YZ, and P and Z are on the same side of line YX. A *triangle* is three points not on one line; its angle at each corner is the angle formed by the rays to the other two corners. A *circle* with center O and radius r > 0 is the set of points at distance r from O. Two points A and T of a circle with center O are *opposite* when O lies between A and T. A line *crosses* two lines when it meets each of them at exactly one point. A line *touches* a circle when it meets the circle at exactly one point, and two circles *touch* when they meet at exactly one point.

### A.2 What is given

These are the facts stated in the problem (Section 5.1).

1. The large circle has center O and radius r > 0, and the line touches it at exactly one point, T.
2. A is on the circle, opposite T: O lies between A and T (definition of opposite). So OA = OT = r (definition of circle) and, by A4, AT = AO + OT = 2r.
3. The smaller circle touches the large circle at B, so B is on the large circle (definition of touching) and OB = r (definition of circle).
4. A, B, C lie on one line, with B between A and C, AB = 14 cm and BC = 6 cm.
5. C is on the line that touches the circle at T. Call it the ground line.

The smaller circle is used only to fix B and C; no step of the proof uses it further. Section A.12 shows that the whole configuration, smaller circle included, exists.

### A.3 Step 0: the points are placed as they need to be

1. AC = AB + BC = 20 cm, by A4 and given 4.
2. A ≠ T: AT = 2r > 0, and the distance from a point to itself is 0 (A4).
3. A is not on the ground line: A is on the circle, A ≠ T, and the ground line meets the circle only at T (given 1).
4. B ≠ A and B ≠ C: AB and BC are positive, and the distance from a point to itself is 0 (A4).
5. B ≠ T. Suppose B = T. Then B and C both lie on the ground line and are distinct (item 4), so by A2 line BC is the ground line. A lies on the line through A, B and C (given 4), which is line BC (A2), so A would be on the ground line, contradicting item 3.
6. B is not on line AT. A, O and T are distinct points of one line (given 2 and A3(e)), which is line AT (A2), and O lies between A and T, so by A4 the only points of line AT at distance r from O are A and T. B is at distance r from O (given 3), and B is neither A (item 4) nor T (item 5).
7. C is not on line AT. A ≠ C, since A is not on the ground line and C is. If C were on line AT, then by A2 line AC would be line AT, and B, which lies on line AC (given 4 and A2), would lie on line AT, contradicting item 6.
8. C ≠ T, since T is on line AT and C is not (item 7).

So A, B, T form a triangle (item 6), and A, T, C form a triangle (item 7). Also O ≠ A and O ≠ T, since OA = OT = r > 0 (A4); so line OA and line OT are both line AT (A2), which does not contain B (item 6). Hence O, A, B form a triangle, and O, B, T form a triangle.

### A.4 Lemma L1: the base angles of an isosceles triangle are equal

Let PQR be a triangle with PQ = PR.

1. Compare triangle PQR with triangle PRQ, the same triangle with its corners read in another order. PQ in the first equals PR in the second; PR in the first equals PQ in the second; the angle at P is the same angle in both.
2. By A6 the two are congruent, with Q matched to R, so their corresponding angles are equal: ∠PQR = ∠PRQ.

### A.5 Lemma L2: the angles of a triangle add to 180°

Let PQR be a triangle with angles p, q, r at P, Q, R.

1. P is not on line QR, since P, Q, R form a triangle. By A8 there is a line m through P parallel to QR. By A4 choose points M and N on m with P between them. Line PQ is not m, since Q is on line PQ and m does not meet QR; so m and line PQ share only P (A2), and neither M nor N is on line PQ, since both differ from P, which lies between them (A3(e)). Segment MN meets line PQ at P, so M and N are on opposite sides of line PQ (A3(b)). R is not on line PQ, so exactly one of the two is on the opposite side from R (A3(b)); call that point M and the other N.
2. Line PQ crosses the parallels m and QR at P and Q: it meets m only at P (step 1), and it meets line QR only at Q, since P is not on line QR, so line PQ is not line QR and two distinct lines share at most one point (A2). M and R lie on opposite sides of line PQ. By A9, ∠MPQ = ∠RQP = q.
3. By A10, N and Q lie on opposite sides of line PR. Line PR crosses the parallels at P and R: R is not on m, since m does not meet line QR, so line PR is not m and meets it only at P; P is not on line QR, so line PR is not line QR and meets it only at R (A2). So by A9, ∠NPR = ∠QRP = r.
4. By A10, ∠MPQ + ∠QPR + ∠RPN = 180°, that is, q + p + r = 180°.

### A.6 Lemma L3: Thales' theorem

*Statement.* If O lies between A and T with OA = OT = r, and B is a point at distance r from O that is not on line AT, then ∠ABT = 90°.

1. OA = OB = OT = r.
2. O lies between A and T, so O is on line AT and differs from A and from T (A3(e)), and line OA and line OT are both line AT (A2). B is not on line AT, so O, A, B form a triangle, and O, B, T form a triangle. In triangle OAB, OA = OB, so by L1, ∠OAB = ∠OBA. Call this α.
3. In triangle OBT, OB = OT, so by L1, ∠OTB = ∠OBT. Call this β.
4. O lies between A and T, so ray AO is ray AT (A3(d)). The angle of triangle ABT at A is formed by ray AB and ray AT, so it is ∠OAB = α.
5. Likewise O lies between T and A (A3(e)), so ray TO is ray TA (A3(d)), and the angle of triangle ABT at T is ∠OTB = β.
6. By A3(c), ray BO lies inside ∠ABT. By A5(a), ∠ABT = ∠ABO + ∠OBT = α + β.
7. By L2, the angles of triangle ABT add to 180°: α + β + (α + β) = 180°.
8. So α + β = 90°, and ∠ABT = 90°.

Every step above holds for every point B at distance r from O that is not on line AT, so the lemma holds for every such B. In our problem, A, O and T satisfy the hypotheses by given 2, and B by given 3 and Step 0, item 6.

### A.7 Lemma L4: the radius to the touching point is perpendicular to the line

1. O is not on the ground line. If it were, then by A4 two points of the ground line would be at distance r from O, so the line would meet the circle twice, contradicting given 1.
2. By A7, draw the perpendicular from O to the ground line; call its foot F. Suppose F ≠ T.
3. F ≠ T, so FT > 0 (A4). By A4 the ground line has exactly two points at distance FT from F, and F lies between them; T is one of them, and T′ is the other. So FT′ = FT and F lies between T and T′. Then T′ ≠ T, since F lies between them (A3(e)).
4. O is not on the ground line (step 1), while F, T and T′ are distinct points on it (F ≠ T by supposition, T′ ≠ F since FT′ = FT > 0 by A4, and T′ ≠ T by step 3), so O, F, T and O, F, T′ form triangles: by A2 the only line through two distinct points of the ground line is the ground line, and O is not on it. ∠OFT = 90°, since line OF is perpendicular to the ground line (A5(c)). T and T′ are distinct points of the ground line, so line TT′ is the ground line (A2), and F lies between T and T′, so by A5(b), ∠OFT′ = 180° − 90° = 90°.
5. Triangles OFT and OFT′ share OF, have FT = FT′, and have equal angles at F. By A6, OT′ = OT = r. So T′ is on the circle and on the ground line, and T′ ≠ T, contradicting given 1. Therefore F = T, and OT is perpendicular to the ground line.
6. C is on the ground line and C ≠ T (Step 0, item 8), so ∠OTC = 90° (A5(c)). O lies between T and A (given 2 and A3(e)), so ray TO is ray TA (A3(d)). Therefore ∠ATC = 90°.

### A.8 Lemma L5: two perpendiculars to one line never meet

Let lines m and n be perpendicular to a line ℓ at distinct points D and T.

1. Suppose m and n meet at a point X.
2. m meets ℓ only at D: m ≠ ℓ, since perpendicular lines are distinct (A5(c)), and two distinct lines share at most one point (A2). Likewise n meets ℓ only at T. Since D ≠ T, X is not on ℓ, and D, T, X form a triangle.
3. The angle of this triangle at D is formed by lines ℓ and m, so it measures 90° (A5(c)); likewise the angle at T. By A5, ∠DXT > 0°. So the three angles add to more than 180°, contradicting L2.
4. Therefore m and n do not meet: by A8 they are parallel.

### A.9 Lemma L6: AT² = AB × AC

1. By A4, choose D on ray AT with AD = AB, and E on ray AC with AE = AT.
2. A, D, E form a triangle: D and E differ from A, since AD = AB > 0 and AE = AT > 0 (A4); and if A, D, E were on one line, then by A2 line AT and line AC would be the same line, contradicting Step 0, item 7.
3. D is on ray AT and D ≠ A, so D = T, or D lies between A and T, or T lies between A and D (definition of ray, and A3(a) and A3(e)). If D = T, ray AD is ray AT; in the other two cases ray AD is ray AT by A3(d). E is on ray AC and E ≠ A (step 2), so E = C, or E lies between A and C, or C lies between A and E (definition of ray, and A3(a) and A3(e)). If E = C, ray AE is ray AC; in the other two cases ray AE is ray AC by A3(d). And ray AC is ray AB because B lies between A and C (A3(d)). So ∠DAE = ∠TAB.
4. In triangles ADE and ABT, AD = AB, AE = AT and ∠DAE = ∠BAT. By A6 they are congruent, with D matched to B and E matched to T, so ∠ADE = ∠ABT.
5. ∠ABT = 90° by L3, so ∠ADE = 90°. And ∠ATC = 90° by L4.
6. D ≠ T. If D were T, then AB = AD = AT, and by L1 triangle ABT would have ∠ATB = ∠ABT = 90°. With ∠BAT > 0° (A5), its angles would add to more than 180°, contradicting L2.
7. Line DE is not line AT, since E is not on line AT (step 2, and line AD is line AT by A2); it meets line AT at D with ∠ADE = 90° (step 5), so it is perpendicular to line AT at D (A5(c)). Line TC is not line AT, since C is not on it (Step 0, item 7), and ∠ATC = 90° (step 5), so it is perpendicular to line AT at T (A5(c)). D ≠ T (step 6). By L5, lines DE and TC are parallel.
8. D and T lie on ray AT; E and C lie on ray AC; the two rays are not on one line (Step 0, item 7). By A11, AD/AT = AE/AC.
9. Substituting AD = AB and AE = AT gives AB/AT = AT/AC. Multiplying both sides by AT × AC (A1) gives AT² = AB × AC.

### A.10 The answer

1. By L6, given 4 and Step 0, item 1, AT² = AB × AC = 14 × 20 = 280.
2. AT = 2r (given 2), so 4r² = 280, and r² = 70.
3. r > 0 (given 1), so by A1, r = √70 cm, about 8.37 cm.

So if the configuration exists, r = √70 cm. Section A.12 shows that it does.

### A.11 Where the parallel postulate enters

Of the foundation, A9 and A11 are the items Euclid proves from his fifth postulate or from results that depend on it. A9 is Elements I.29 itself. A11 rests on Elements VI.1 and VI.2, whose proofs use Euclid's results on parallelograms and triangles between parallels (I.34 to I.38), which depend on I.29. The proof uses A9 through L2, on which L3, L5 and L6 depend, and uses A11 in L6. A8 also mentions parallel lines, but Euclid constructs a parallel without the fifth postulate (Elements I.31). A10 mentions a parallel line. It is assumed here, and this paper does not show whether it depends on the fifth postulate. All references are to Ref. 10.

### A.12 The configuration exists

Sections A.3 to A.10 show that if the configuration of Section 5.1 exists, then r = √70 cm. This section shows that it exists, using coordinates (A12). Lengths are in centimeters. Write r = √70 and c = √120, so r² = 70 and c² = 120. For numbers that are not negative, equal squares give equal numbers (A1): if both are positive, A1's one positive square root makes them equal; if one is 0, so is the other.

1. **The points.** Let T = (0, 0), O = (0, r), A = (0, 2r), C = (c, 0), B = (7c/10, 3r/5) and Q = (c, 3r/7), and let s = 3r/7. The large circle has center O and radius r. The smaller circle has center Q and radius s, and 0 < s < r, since s = 3r/7 and r = √70 > 0 (A1). The ground line is the line through T and C (A2). By A12 it is the set of points with ax + by = k, a and b not both 0; T gives k = 0, and C gives ac = 0, so a = 0, since c = √120 > 0 (A1); then b ≠ 0, so the ground line is the set of points with y = 0.
2. **The ground line touches the large circle only at T.** A point (x, 0) is on the large circle when x² + (0 − r)² = r² (definition of circle, A12 and A1), that is, x² = 0, so x = 0 (A1). The only such point is T, and T is on the large circle: 0² + (0 − r)² = r².
3. **A is opposite T.** O = A + ½(T − A), so O lies between A and T (A12), and A is opposite T (definition of opposite). OA² = 0² + (2r − r)² = r² and OT² = 0² + (0 − r)² = r², so OA = OT = r, since a distance is the positive square root (A12 and A1) and r > 0 (item 1).
4. **B is on the large circle.** OB² = (7c/10)² + (3r/5 − r)² = 49c²/100 + 4r²/25 = 49 × 120/100 + 4 × 70/25 = 58.8 + 11.2 = 70 = r², so OB = r, since a distance is the positive square root (A12 and A1) and r > 0 (item 1).
5. **A, B, C lie on one line, with B between A and C, AB = 14 and BC = 6.** C − A = (c, −2r), and A + (7/10)(C − A) = (7c/10, 2r − 7r/5) = (7c/10, 3r/5) = B, so B lies between A and C (A12), and therefore A, B and C lie on one line (A3(e)). As a check, all three satisfy 2r·x + c·y = 2rc: for A, 0 + 2rc = 2rc; for C, 2rc + 0 = 2rc; for B, 14rc/10 + 6rc/10 = 2rc. AC² = c² + (2r)² = 120 + 280 = 400, so AC = 20 (A12 and A1). For any t > 0 and any (u, v) other than (0, 0), so that u² + v² > 0 (A1), the distance formula gives √((tu)² + (tv)²) = t√(u² + v²), since t√(u² + v²) is positive and its square is (tu)² + (tv)² (A12 and A1). Since B − A = (7/10)(C − A), this gives AB = (7/10) × 20 = 14, and since C − B = (3/10)(C − A), it gives BC = (3/10) × 20 = 6.
6. **The smaller circle touches the ground line only at C.** A point (x, 0) is on the smaller circle when (x − c)² + (0 − s)² = s² (definition of circle, A12 and A1), that is, (x − c)² = 0, so x = c (A1). The only such point is C, and C is on the smaller circle: (c − c)² + (0 − s)² = s².
7. **B is on the smaller circle.** QB² = (c − 7c/10)² + (3r/7 − 3r/5)² = 9c²/100 + 36r²/1225 = 9 × 120/100 + 36 × 70/1225 = 54/5 + 72/35 = 90/7, and s² = 9r²/49 = 630/49 = 90/7. So QB = s, since a distance is the positive square root (A12 and A1) and s > 0 (item 1).
8. **The two circles meet only at B.** Let (x, y) be on both circles. Then x² + (y − r)² = r² and (x − c)² + (y − s)² = s² (definition of circle, A12 and A1), which expand to x² + y² − 2ry = 0 and x² + y² − 2cx − 2sy + c² = 0. Subtracting the second from the first gives 2cx − 2(r − s)y − c² = 0. Since r − s = 4r/7, this is x = c/2 + 4ry/(7c). Then x² = c²/4 + 4ry/7 + 16r²y²/(49c²) = 30 + 4ry/7 + 4y²/21, using c² = 120 and r² = 70. Putting this into x² + y² − 2ry = 0 gives 30 − 10ry/7 + 25y²/21 = 0. Multiplying by 21/5 gives 5y² − 6ry + 126 = 0, and since 5(3r/5)² = 9r²/5 = 126, this is 5(y − 3r/5)² = 0. So y = 3r/5 (A1), and x = c/2 + 12r²/(35c) = c/2 + 24/c = (c² + 48)/(2c) = 84/c = 7c/10. The only common point is B, so the circles touch at B (definition of touching).

So the configuration exists, with r = √70 cm, and by A.10 no other value of r is possible. The smaller circle has radius 3√70/7 cm, about 3.59 cm.

## Appendix B. The first answer, as given

The first answer was an interactive figure with five views, each with a caption and a list of statements beside their values. Its text is reproduced here as it was shown for AB = 14 and BC = 6. Section 5.3 refers to it.

**Setup.** Caption: "Facts used: the big circle touches the line at T. A is the point opposite T, so AT is a diameter (AT = 2r) and AT is perpendicular to the line. A, B, C lie on one straight line. The small circle's size is never needed."

| Statement | Value |
| --- | --- |
| AC = AB + BC | 14 + 6 = 20 |
| AT = 2r (diameter) | unknown |
| AT ⟂ line (radius to tangent point) | ∠ATC = 90° |

**1. Right angle at B.** Caption: "O is the centre, so OA = OB = OT = r. Triangles OAB and OBT are isosceles. The angles of triangle ABT add to 180°, which forces the angle at B to be 90°."

| Statement | Value |
| --- | --- |
| ∠OAB = ∠OBA = α (OA = OB) | isosceles |
| ∠OBT = ∠OTB = β (OB = OT) | isosceles |
| Angles of △ABT: 2α + 2β = 180° | α + β = 90° |
| ∠ABT = α + β | 90° |

**2. Similar triangles.** Caption: "Triangle ABT (orange) and triangle ATC (teal) share the angle at A, and each has a right angle (at B and at T). So they are similar, and their sides are in the same ratio."

| Statement | Value |
| --- | --- |
| ∠BAT = ∠TAC (same angle at A) | shared |
| ∠ABT = ∠ATC | 90° = 90° |
| So △ABT \~ △ATC, and AB/AT = AT/AC | AB × AC = AT² |
| AT² = AB × AC | 14 × 20 = 280 |

**3. Solve for r.** Caption: "Put the numbers into AT² = AB × AC with AT = 2r."

| Statement | Value |
| --- | --- |
| (2r)² = AB × AC | 4r² = 280 |
| r² = AB × AC ÷ 4 | 280 ÷ 4 = 70 |
| r | √70 ≈ 8.37 |

**4. Check another way.** Caption: "Independent check. CT is tangent to the big circle at T, so CT² = CB × CA (tangent and secant from C). Then Pythagoras in triangle ATC gives AT² again."

| Statement | Value |
| --- | --- |
| CT² = CB × CA | 6 × 20 = 120 |
| AT² = AC² − CT² | 20² − 120 = 280 |
| Same as step 2 | AT² = 280, r = √70 ≈ 8.37 |

## Appendix C. How this paper was made

This paper was written with Claude, an AI system made by Anthropic. The collaboration is an instance of Section 9.4, and I describe it so that a reader can judge the paper and the method together.

### C.1 Who did what

- **I** posed the problems, set the standard, asked the questions in Section 5, made every decision about content and structure, and own every claim in the paper.
- **Claude** drafted the proofs, built the interactive figures, found and read the sources I did not supply at first (Tao's posts, Ref. 3, which I later supplied in full; the Advisory Group's announcement, Ref. 9), and drafted the text from our discussion, in my voice, at my direction.
- **The ideas** in Sections 2, 4 and 6 are mine: that the duty to answer meets the declaration's complaints, that it covers every question whatever its tone, critique or validity, that it applies to everyone, and that it continues after publication. The three-part wording of requirements 1 to 3 (state the foundation, leave no gap above it, go deeper when asked) was first written by Claude during our discussion; I adopted it and extended it to any depth the questioner asks.

**Disclosure.** Claude is made by Anthropic, which employs Levent Alpöge, one of the two mathematicians in the attribution dispute of Section 6.3. I note it so that the reader can weigh that account.

### C.2 The working rules

1. Claude explains in detail what it is about to do and waits for my approval before acting. When a task has several steps, it does only the approved one, then proposes the next.
2. Claude says which document and which version it is working from before analyzing or editing it. New files carry a date and a version number.
3. Claude does not re-raise a decision I have made, and searches our earlier work before treating anything as unsettled.
4. Every piece of mathematics is held to the standard in Section 4. When Claude assesses a proof, it lists every gap and lists false steps separately.
5. Claude tests an evaluative word, such as "strong" or "damaging," against the evidence before using it.
6. Claude checks that every cited source says what it is cited for.

### C.3 Where the collaboration failed, and what caught it

The failures are part of the evidence, so I list them.

- **July 2026.** Asked whether a mathematical paper proved its results, Claude said it did, then listed defective steps in the same answer. Under questioning it emerged that at thirteen places Claude had carried out a missing derivation itself, found that it worked, and credited the paper with it. Rule 4 above is the rule against that. The record of that exchange is not reproduced in this paper.
- **27 September 2026, the squares problem.** The symmetry argument I rejected, and the circular step Claude found in its own argument (Section 5.5).
- **30 September 2026, the circle problem.** The seven questions of Section 5.3, in full in Appendix D. Five of them exposed a defect in work Claude had presented as finished; Section 5.3 says what the other two did.
- **30 September 2026, this paper's argument.** Twice Claude presented points I had already answered as open objections a critic might raise. Both times it had itself written my answer. I rejected both framings.
- **Sources.** Claude's web tool returns pages through a summarizer, which on first reading left out the most important sentence of the Advisory Group's recommendations and turned a paraphrase in MIT Technology Review into a false quotation. I then supplied the full texts of every source quoted here, including Tao's posts, and Claude checked each quotation against these texts word for word. The date of Tao's clarification, 5 September, did not copy over with its text; I confirmed it on the post itself. Claude also read the Advisory Group's announcement (Ref. 9) directly. MIT Technology Review reports Bubeck's statement without quoting him, and this paper gives it as the article's report.
- **Draft v2.** After two audits by Claude, two independent reviews of Draft v2, one by a separate Claude agent that had not seen our discussion and one by Grok, found many further gaps, false steps and overstatements, several of them structural. Draft v3 was rebuilt in full in response.
- **Draft v3.** A further independent review by a Claude agent, one by Grok, and a check of every claim against its sources found errors that the earlier audits had missed: a misquotation of my own seventh question, a sentence of MIT Technology Review attributed to Bubeck, a misreport of what the Advisory Group asks about access to models, a date with no source, a contradiction between Sections 6.1 and 8.3 of Draft v3, and claims larger than their evidence. Draft v4 corrected them.
- **Draft v4.** Draft v4 cited Fallis from an encyclopedia's quotation of him. Reading his article showed a wrong page number and a misstatement of his position: his account is descriptive, and he takes no side on whether gaps should be allowed. Reading the work on proofs as dialogue showed that the idea of a proof answering questions, in depth, was already set out by Krabbe and by Dutilh Novaes, and Draft v4 credited neither. Draft v5 corrected both and said what the standard adds.
- **Draft v5.** Two independent reviews of Draft v5, one by a Claude agent and one by Grok, found that the case study contradicted its own record: Draft v5 said that every question exposed a defect, and Appendix D shows that two did not. They also found that a revision in Draft v4 had deleted the Advisory Group quotation on which Section 4.2 rests, that notes in Appendix D withdrew claims while leaving other copies of them in place, that several of my proposals were stated as established facts, and small breaks in Appendix A. Draft v6 corrected the claims and notes the reviews identified, stated those proposals as proposals, and was checked sentence by sentence against Draft v5.
- **Draft v6.** Eight reviews by fresh Claude agents and five by Grok examined Draft v6, revisions 61 to 68. They found seven false steps or contradictions, each fixed by revision 68 and listed in the [review record](https://claude.ai/artifact/JTk7pC7YYrEirEm7ueHWb9), published as a separate document. One was a condition for moving a result from course 2.B to course 2.A that the four requirements did not contain; it led me to make understanding part of requirement 3. Reviews of the record later showed that at least seven findings those reviews had not listed as false steps were false steps too; revision 65 had fixed three of them, revision 71 three more, and revision 77 the seventh. The review record answers the findings of the reviews of Draft v6 and describes the corrections that the reviews of the record led to; it also says which accepted findings were corrected in the text, and in which revision. Revision 83 added three earlier documents as precedents (Refs. 21 to 23), and that revision and later ones described them in places in ways they do not bear out; the review record, Part 6, lists each finding and its answer, with the revision that corrected the text where one did.

### C.4 What made it work

The rule was that no answer is accepted until it survives questioning, and that Claude's answers count only when the missing step is on the page. The rule was not always kept: Appendix C.3 lists answers that were accepted and later found wrong. The same method was applied to the paper's proofs, and independent review applied it to the paper's argument. Nothing in the paper is published until I am prepared to answer for it, with or without the AI.

## Appendix D. The exchange about the circle problem

This is the whole exchange of 30 September 2026 about the circle problem, in order, as recorded in the session. My messages are quoted as I typed them, except that strong language is omitted and marked "...". Claude's replies are given as written, including their spelling. Each reply is referred to by the time of the message it answers. Claims in Claude's replies that carry no note are recorded as made, not endorsed by this paper. Each interactive figure is given as its text, as shown for AB = 14 and BC = 6; the drawings are not reproduced. Notes added during the revision of this paper are in square brackets. The labels A1 to A7 in the last reply are that reply's own and differ from those of Appendix A; for example, its A3 is Appendix A's A6. Its L1 to L6 name the same lemmas as L1 to L6 in Appendix A. The labels F1 to F6 in the 07:47 reply are that reply's own. The proof in Appendix A grew out of the last reply here, through further questioning during the writing of this paper.

**Me, 07:17.** "Here's another problem. I want it solved methodically as we've done it previously." (The problem was attached as an image. Section 5.1 states it in full.)

**Claude.** I'll solve it the way we did the squares. First I state which facts come from the problem and which would come only from the drawing. Then I go step by step, with the picture and the live formulas together. Sliders let you change AB and BC and watch every formula update.

*Interactive figure. Its text is given in Appendix B.*

The answer is **r = √70 cm ≈ 8.37 cm**. The key relation is (2r)² = AB × AC = 14 × 20 = 280.

The solution needs three facts. The problem states none of them in words, so they have to be read off the picture. Students should be told to accept these as given:

1. The big circle touches the line at a point T.
2. A is the point directly opposite T, the top of the circle. In the picture it is drawn above the centre.
3. A, B and C lie on one straight line, the green segment.

Nothing else depends on how the picture is drawn. In particular, the small circle's size never enters the calculation. Its only job is to explain where B and C are. Its radius comes out afterwards as r × BC/AB = 3√70/7 ≈ 3.59 cm, which confirms that the given lengths fit together.

Step 4 is there for students who doubt the similar-triangles step. It reaches AT² = 280 by a separate route, the tangent-secant rule plus Pythagoras.

**Me, 07:23.** "You didn't explain the key relationship! Why?"

**Claude.** The widget stated the key relationship but never explained it. Step 2 said "So △ABT \~ △ATC, and AB/AT = AT/AC" and moved on. It never said which vertex matches which vertex, so it never showed why AB is paired with AT and AT is paired with AC. By your proof standard, that line is an assignment, not a step. I also found three other breaks, listed at the end. Here is the key relationship with every step shown.

**Claim:** AT² = AB × AC

**Step 1. The angle at B is a right angle.**

1. A is the point opposite T, so AT is a diameter and its midpoint is the centre O. Then OA = OB = OT = r.
2. Triangle OAB has OA = OB, so its base angles are equal. Call them α: ∠OAB = ∠OBA = α.
3. Triangle OBT has OB = OT, so ∠OBT = ∠OTB. Call them β.
4. O lies on segment AT, so the angle of triangle ABT at A is ∠OAB = α, and its angle at T is ∠OTB = β.
5. O lies on AT, which is the side of triangle ABT opposite B, so the ray BO runs between BA and BT. That makes ∠ABT = ∠ABO + ∠OBT = α + β.
6. The angles of triangle ABT add to 180°: α + β + (α + β) = 180°. So α + β = 90°, which means ∠ABT = 90°.

**Step 2. The angle at T is a right angle.** The line touches the circle only at T. Suppose OT were not perpendicular to the line. Then the foot F of the perpendicular from O to the line would be a different point, with OF < OT = r. So F would lie inside the circle, and the line would cross the circle at two points, which contradicts touching it only at T. Therefore ∠ATC = 90°.

**Step 3. Match the two triangles vertex by vertex.** Compare triangle ABT with triangle ATC.

- **At A:** B lies on segment AC, so rays AB and AC are the same ray. So ∠BAT = ∠CAT.
- **Right angles:** ∠ABT = 90° (step 1) and ∠ATC = 90° (step 2).
- **Third angles:** each is 180° minus the angle at A minus 90°, so ∠ATB = ∠ACT.

So the vertices match as **A → A, B → T, T → C**, and △ABT \~ △ATC in exactly that order.

**Step 4. Read off matching sides.** With that matching, each side of △ABT pairs with the side joining the matched vertices:

- AB (A to B) pairs with AT (A to T).
- AT (A to T) pairs with AC (A to C). Both are hypotenuses.
- BT pairs with TC.

Similar triangles have equal ratios of matching sides, so AB / AT = AT / AC.

**Step 5. Clear the fractions.** Multiply both sides by AT × AC to get **AB × AC = AT²**. In words, the diameter AT is the geometric mean of AB and AC.

**Step 6. Put in the numbers.** AC = 14 + 6 = 20, so AT² = 14 × 20 = 280. With AT = 2r, this gives 4r² = 280, so r² = 70 and **r = √70 ≈ 8.37 cm**.

**Other breaks in the widget**

- **Step 1** said "the angles add to 180°, which forces 90°" without steps 4 and 5 above. Those are what connect α and β to the angles of triangle ABT.
- **Setup** stated "AT ⟂ line" as a fact, with no argument like step 2 above.
- **Step 4 of the widget** called the tangent-secant check "independent", and it isn't. The tangent-secant rule is itself proved with a similar pair of triangles (△CBT \~ △CTA), and the widget cited it without proof. That is another assignment, and the word "independent" was false. \[Note added in revision: this exchange does not prove that claim about the tangent-secant rule, and the sentence before this note rests on it. Section 5.3 records only that the rule was cited without proof.\]

I propose rebuilding the widget with steps 1 to 5 above as its steps. Each step would show the vertex correspondence drawn on the figure: matched vertices in the same colour, matched sides highlighted in pairs. The "check" step would either be removed or replaced by a proved version labelled as a second use of the same method. Shall I go ahead?

**Me, 07:25.** "Redo the whole thing! ... You skip steps! Do it right!"

**Claude.** I'm rebuilding it from scratch. Every step now shows its reasoning on the page, and the figure and the live values change together. I dropped the old "check" step because it depended on a rule it never proved.

*Interactive figure, eight steps with buttons. Its text, as shown for AB = 14 and BC = 6:*

**Given.** Caption: "Everything the proof uses is listed here. Nothing else is read from the drawing. The small circle is needed only to place B and C."

| Statement and reason | Value |
| --- | --- |
| AB and BC (given) | AB = 14, BC = 6 |
| A, B, C lie on one straight line with B between A and C, so AC = AB + BC | 14 + 6 = 20 |
| The big circle touches the line at exactly one point, T |  |
| A is the point of the big circle opposite T, so AT is a diameter and its midpoint is the centre O | AT = 2r |
| The two circles touch at B, so B lies on the big circle |  |
| Goal: find r |  |

**1. Equal angles.** Caption: "Draw the radius OB. All three of OA, OB and OT are radii, so two isosceles triangles appear. Their base angles are equal in pairs: α (amber) and β (teal)."

| Statement and reason | Value |
| --- | --- |
| OA, OB, OT are radii of the big circle | OA = OB = OT = r |
| In triangle OAB, OA = OB, so the angles opposite them are equal: ∠OAB = ∠OBA. Call this α. | α = 33.2° |
| In triangle OBT, OB = OT, so ∠OBT = ∠OTB. Call this β. | β = 56.8° |

**2. Right angle at B.** Caption: "Now look at the whole triangle ABT. Its angle at A is α, its angle at T is β, and its angle at B is split by OB into α and β. Adding the three angles gives the right angle at B."

| Statement and reason | Value |
| --- | --- |
| O lies on AT, so the ray from A through O is the ray AT. Hence ∠BAT = ∠OAB. | ∠BAT = α = 33.2° |
| Likewise the ray from T through O is the ray TA. Hence ∠BTA = ∠OTB. | ∠BTA = β = 56.8° |
| O lies on side AT, opposite B, so ray BO lies inside ∠ABT and splits it. | ∠ABT = α + β |
| The angles of triangle ABT add to 180°. | α + β + (α + β) = 180° |
| Divide by 2. | α + β = 90° |
| Therefore ∠ABT = 90°. | 33.2° + 56.8° = 90° |

**3. Right angle at T.** Caption: "A radius meets the line at the touching point at a right angle. The proof is by contradiction: if it did not, the line would meet the circle at a second point."

| Statement and reason | Value |
| --- | --- |
| Suppose OT is not perpendicular to the line. Drop the perpendicular from O to the line; its foot F is then a point other than T. | assume |
| Mark T′ on the line on the other side of F, with FT′ = FT. |  |
| Triangles OFT and OFT′ share OF, have FT = FT′, and have right angles at F, so they are congruent (side, angle, side). | OT′ = OT = r |
| So T′ lies on the circle and on the line, and T′ ≠ T. The line would touch the circle at two points, contradicting the given. | contradiction |
| Therefore OT is perpendicular to the line. Since A, O, T are on one line, ∠ATC = 90°. | ∠ATC = 90° |

**4. Matching angles.** Caption: "Compare triangle ABT (orange) with triangle ATC (teal). They have the same angle at A (purple), a right angle each, and so the same third angle (double arc)."

| Statement and reason | Value |
| --- | --- |
| B lies between A and C, so ray AB is the same ray as AC. The angle at A is the same in both triangles (purple). | ∠BAT = ∠CAT = 33.2° |
| Right angles: step 2 and step 3. | ∠ABT = ∠ATC = 90° |
| Third angle of triangle ABT: the angles add to 180°. | ∠ATB = 180° − 33.2° − 90° = 56.8° |
| Third angle of triangle ATC: the angles add to 180°. | ∠ACT = 180° − 33.2° − 90° = 56.8° |
| All three angles match (double arcs are equal). | ∠ATB = ∠ACT |

**5. Matching vertices.** Caption: "Equal angles tell us which vertex goes with which: A with A, B with T, T with C. Below, both triangles are redrawn in the same position so the matching is visible. Matching sides have the same colour."

| Statement and reason | Value |
| --- | --- |
| Angle at A in triangle ABT matches angle at A in triangle ATC | A → A |
| Right angle at B matches right angle at T | B → T |
| Third angle at T matches third angle at C | T → C |
| A side joins two vertices, so it matches the side joining their partners. A–B matches A–T (purple). | AB ↔ AT |
| B–T matches T–C (orange). | BT ↔ TC |
| A–T matches A–C (teal). Both are opposite the right angle. | AT ↔ AC |

**6. Ratio of sides.** Caption: "Triangles with the same angles have their matching sides in the same ratio. Take the ratio of the purple pair and the teal pair."

| Statement and reason | Value |
| --- | --- |
| Two triangles with the same three angles are similar: every side of one is the same multiple of its matching side in the other. |  |
| Purple pair: AB in triangle ABT, AT in triangle ATC. | AB / AT = 14 / 16.73 = 0.837 |
| Teal pair: AT in triangle ABT, AC in triangle ATC. | AT / AC = 16.73 / 20 = 0.837 |
| The two ratios are equal. | AB / AT = AT / AC |

**7. Solve for r.** Caption: "Clear the fractions, then use AT = 2r."

| Statement and reason | Value |
| --- | --- |
| Start from step 6. | AB / AT = AT / AC |
| Multiply both sides by AT × AC. | AB × AC = AT² |
| Put in AB and AC from the Given step. | AT² = 14 × 20 = 280 |
| AT is a diameter, so AT = 2r and AT² = 4r². | 4r² = 280 |
| Divide by 4. | r² = 70 |
| Take the positive square root. | r = √70 ≈ 8.37 |

It's rebuilt as eight steps. Each row on the right gives a statement and its reason, so the reader never has to fill in a missing step.

- **Given** lists every fact the proof uses, including the three that come only from the drawing: A is opposite T, A, B and C lie on one line, and the circles touch at B.
- **Steps 1 and 2** prove the right angle at B. The widget labels each angle, shows why the angle at B splits into α + β, and adds up the angles of triangle ABT.
- **Step 3** proves the right angle at T by contradiction. It no longer just states it.
- **Steps 4 and 5** match the angles, then pair the vertices: A with A, B with T, T with C. Both triangles are redrawn in the same position, and matching sides have the same colour.
- **Steps 6 and 7** take the two ratios and solve. The result is r = √70 ≈ 8.37 cm.

Next and Previous buttons at the bottom move through the steps in order. The AB and BC sliders update every value.

**Me, 07:30.** "Why is ∠ABT = 90º? This is not explained!!!!"

**Claude.** The angle at B is 90° because A and T are the two ends of a diameter. Here is the complete argument, with the picture and the equations together:

*Figure: Circle with diameter AT and centre O, point B on the circle. Radius OB splits triangle ABT into two isosceles triangles with base angles alpha and beta.*

Text beside the figure:

> OA = OB = OT = r △OAB: OA = OB, so ∠OAB = ∠OBA = α △OBT: OB = OT, so ∠OTB = ∠OBT = β Angles of △ABT: at A: α, at T: β at B: α + β α + β + (α + β) = 180° 2(α + β) = 180° ∠ABT = α + β = 90°

Each line in the picture, with its reason:

1. **Three equal lengths.** O is the centre. A, B and T all lie on the circle, so OA = OB = OT = r.
2. **Triangle OAB has two equal sides, OA and OB.** In a triangle, the angles opposite equal sides are equal. So ∠OAB = ∠OBA. Call this angle α.
3. **Triangle OBT has two equal sides, OB and OT.** For the same reason, ∠OTB = ∠OBT. Call this angle β.
4. **The angle of triangle ABT at A is α.** O lies on segment AT, so the ray from A toward O is the same ray as the one from A toward T. That makes ∠BAT and ∠OAB the same angle.
5. **The angle of triangle ABT at T is β.** By the same reasoning from the other end, the ray from T toward O is the ray toward A, so ∠BTA and ∠OTB are the same angle.
6. **The angle at B is α + β.** O lies on the side AT, which is opposite B. So the segment BO runs inside the angle at B and splits it into ∠ABO = α and ∠OBT = β.
7. **Add the three angles of triangle ABT.** They total 180°: α + β + (α + β) = 180°.
8. **Solve.** 2(α + β) = 180°, so α + β = 90°. From step 6, that sum is ∠ABT, so **∠ABT = 90°**.

The only thing this uses about B is that it lies on the circle. AT is a diameter, so this works for any point B on the circle. This result is known as Thales' theorem.

**Me, 07:31.** "Why didn't you note this!!!!! At the beginning!!!! This is what I'm telling you. You don't keep key steps in!!!! Redo the whole things correctly this time!!!!"

**Claude.** I'm redoing the whole solution as one page. At the top is a plan that names the three key facts before they're used. Every step is visible at once, each with its own picture and a full list of statements and reasons, so nothing sits behind a button.

*Interactive figure, one page. Its text, as shown for AB = 14 and BC = 6:*

The plan We want r. The whole solution rests on three key facts, each proved below:

- Key fact 1 (Thales' theorem). If AT is a diameter and B is any point on the circle, then ∠ABT = 90°.
- Key fact 2 (tangent and radius). The radius to the touching point is perpendicular to the line, so ∠ATC = 90°.
- Key fact 3 (similar triangles). Facts 1 and 2 make triangles ABT and ATC similar, which gives AT² = AB × AC. Then AT = 2r turns AT² = AB × AC into an equation for r.

**Step 0. What is given.** These are all the facts the proof uses. The last three come from the drawing, so we state them openly.

| Statement and reason | Value |
| --- | --- |
| AB and BC are given. | AB = 14, BC = 6 |
| The big circle touches the line at exactly one point. Call it T. |  |
| From the drawing: A is the point of the big circle opposite T. So AT is a diameter, its midpoint is the centre O, and AT = 2r. | AT = 2r |
| From the drawing: A, B, C lie on one straight line, with B between A and C. So AC = AB + BC. | AC = 14 + 6 = 20 |
| From the drawing: the two circles touch at B, so B lies on the big circle. |  |

**Step 1. Key fact 1: ∠ABT = 90°.** Draw the radius OB. It splits triangle ABT into two isosceles triangles.

| Statement and reason | Value |
| --- | --- |
| A, B, T lie on the circle with centre O, so OA, OB, OT are radii. | OA = OB = OT = r |
| Triangle OAB has OA = OB. Angles opposite equal sides are equal, so ∠OAB = ∠OBA. Call this α. | α = 33.2° |
| Triangle OBT has OB = OT. For the same reason ∠OTB = ∠OBT. Call this β. | β = 56.8° |
| O lies on AT, so the ray from A toward O is the ray from A toward T. Hence the angle of triangle ABT at A is ∠OAB. | ∠BAT = α |
| Likewise the ray from T toward O is the ray from T toward A. Hence the angle of triangle ABT at T is ∠OTB. | ∠BTA = β |
| O lies on side AT, which is opposite B, so segment BO runs inside the angle at B and splits it into ∠ABO and ∠OBT. | ∠ABT = α + β |
| The three angles of triangle ABT add to 180°. | α + β + (α + β) = 180° |
| So 2(α + β) = 180°, and α + β = 90°. | 33.2° + 56.8° = 90° |
| Therefore ∠ABT = 90°. Only "B is on the circle" was used, so this holds for every point B on the circle. | ∠ABT = 90° |

**Step 2. Key fact 2: ∠ATC = 90°.** Proof by contradiction. Left: what would happen if OT were not perpendicular to the line. Right: the only possibility left.

| Statement and reason | Value |
| --- | --- |
| Suppose OT were not perpendicular to the line. Drop the perpendicular from O to the line. Its foot F would then be a point other than T. | assume, for contradiction |
| Mark T′ on the line on the other side of F, with FT′ = FT. | FT′ = FT |
| Triangles OFT and OFT′ share side OF, have FT = FT′, and both have a right angle at F. So they are congruent (side, angle, side), and OT′ = OT. | OT′ = r |
| So T′ is on the circle and on the line, and T′ ≠ T. The line would meet the circle at two points, but it touches only at T. | contradiction |
| Therefore OT is perpendicular to the line. A, O, T lie on one line and C is on the line, so ∠ATC = 90°. | ∠ATC = 90° |

**Step 3. The two triangles have the same angles.** Triangle ABT (orange) and triangle ATC (teal).

| Statement and reason | Value |
| --- | --- |
| B lies between A and C, so the ray from A through B is the ray from A through C. The two triangles have the same angle at A (purple). | ∠BAT = ∠CAT = 33.2° |
| Step 1 gives the right angle of triangle ABT at B. Step 2 gives the right angle of triangle ATC at T. | ∠ABT = ∠ATC = 90° |
| The angles of triangle ABT add to 180°, so its third angle is 180° minus the other two. | ∠ATB = 180° − 33.2° − 90° = 56.8° |
| The same for triangle ATC. | ∠ACT = 180° − 33.2° − 90° = 56.8° |
| All three angles match (the double arcs are equal). | ∠ATB = ∠ACT |

**Step 4. Key fact 3, part 1: which vertex matches which.** Both triangles redrawn in the same position. Matching vertices and matching sides have the same colour.

| Statement and reason | Value |
| --- | --- |
| Angle at A in triangle ABT matches angle at A in triangle ATC. | A → A |
| Right angle at B matches right angle at T. | B → T |
| Third angle at T matches third angle at C. | T → C |
| A side joins two vertices, so it matches the side joining their partners. Side A–B matches side A–T (purple). | AB ↔ AT |
| Side B–T matches side T–C (orange). | BT ↔ TC |
| Side A–T matches side A–C (teal). Both are opposite the right angle. | AT ↔ AC |

**Step 5. Key fact 3, part 2: AT² = AB × AC.** Similar triangles have their matching sides in the same ratio.

| Statement and reason | Value |
| --- | --- |
| Two triangles with the same three angles are similar: each side of one is the same multiple of its matching side in the other. So the ratios of matching sides are equal. |  |
| Purple pair: AB in triangle ABT over its match AT in triangle ATC. | AB / AT = 14 / 16.73 = 0.837 |
| Teal pair: AT in triangle ABT over its match AC in triangle ATC. | AT / AC = 16.73 / 20 = 0.837 |
| The two ratios are equal. | AB / AT = AT / AC |
| Multiply both sides by AT × AC. | AB × AC = AT² |

**Step 6. Solve for r.** AT is the diameter, so AT = 2r.

| Statement and reason | Value |
| --- | --- |
| Step 5, with AB and AC from Step 0. | AT² = 14 × 20 = 280 |
| AT = 2r (Step 0), so AT² = (2r)² = 4r². | 4r² = 280 |
| Divide both sides by 4. | r² = 280 ÷ 4 = 70 |
| r is a length, so take the positive square root. | r = √70 ≈ 8.37 |

I rebuilt it as a single page that reads from top to bottom.

- **The plan comes first.** Before any work, it names the three key facts the solution rests on: Thales' theorem (∠ABT = 90°), the radius meeting the tangent line at a right angle (∠ATC = 90°), and the similar triangles that give AT² = AB × AC.
- **Every step is visible at once.** Each one has its own picture and a full list of statements and reasons, and nothing is hidden behind buttons.
- **Step 1 is the full Thales proof** you asked about, all nine lines.
- **Step 2 draws the contradiction.** It shows the second point T′ that would appear if OT were not perpendicular to the line.
- **Every later step names the step it relies on.** For example, "Step 1 gives the right angle at B".

The AB and BC sliders at the top update every picture and every value on the page. With AB = 14 and BC = 6, the answer is r = √70 ≈ 8.37 cm.

**Me, 07:43.** "Why isn't Thales theorem mentioned?"

**Claude.** Thales' theorem is named once, in the plan box at the top: "Key fact 1 (Thales' theorem). If AT is a diameter and B is any point on the circle, then ∠ABT = 90°." But I left the name off the place where the theorem is actually proved and used, so the omission is mine. Specifically:

- The **Step 1 heading** says only "Key fact 1: ∠ABT = 90°", with no name.
- Step 1 never **states the theorem before proving it**, so the reader starts the proof without knowing what is being proved in general.
- The **last line of Step 1** proves the general statement ("this holds for every point B on the circle") without saying that this is Thales' theorem.
- **Step 3**, where the right angle is used, says "Step 1 gives the right angle" instead of "Thales' theorem (Step 1) gives the right angle".

I propose these changes to the widget, and nothing else:

1. Rename the Step 1 heading to **"Step 1. Thales' theorem: ∠ABT = 90°"**.
2. Add a first row to Step 1 that states the theorem in full: *"Thales' theorem: if AT is a diameter of a circle and B is any other point on the circle, then ∠ABT = 90°. We prove it for our figure."*
3. Change Step 1's last row to: *"Therefore ∠ABT = 90°. Only 'B is on the circle' was used, so this proves Thales' theorem for every point B on the circle."*
4. In Step 3, change the reference to *"Thales' theorem (Step 1) gives the right angle at B."*
5. Name the other two key facts the same way, in their headings and wherever they are used: "the radius meets the tangent at a right angle" in Step 2, and "similar triangles" in Steps 4 and 5.

Shall I make these changes?

**Me, 07:45.** "Did we prove Thales' theorem?"

**Claude.** Yes, with one gap. Step 1 of the current widget proves Thales' theorem, but the proof uses a fact it never states, and it also leans on three standard results that it cites without proving. By your standard, here is the exact account.

**What Step 1 proves.** It derives ∠ABT = 90° using only these facts:

- B lies on the circle.
- O is the midpoint of AT.
- Three standard facts, listed below.

It never uses anything else about B, so the argument works for every point B on the circle. That general statement is Thales' theorem. So Step 1 is a proof of it, not just a use of it.

**The break: a missing fact.** The proof needs B to be different from A and from T, so that B does not lie on the line AT. Otherwise triangles OAB, OBT and ABT don't exist. Step 1 never says this. For our figure it holds, for two reasons:

- **B ≠ A**, because AB = 14 > 0.
- **B ≠ T.** Suppose B = T. Then the line through B and C would be the line through T and C, which is the ground line, since T and C both lie on it. A is not on the ground line, so A, B and C could not lie on one straight line, which contradicts what is given.

If B were on the line AT but different from A and T, that line would meet the circle at three points, and a line meets a circle at most twice. So B is not on line AT. None of this is on the page.

**Cited, not proved.** Step 1 relies on three standard results:

1. **Isosceles base angles:** in a triangle, the angles opposite equal sides are equal. This is Euclid I.5.
2. **Angle sum:** the angles of a triangle add to 180°. This is Euclid I.32.
3. **Angle addition:** a ray inside an angle splits it into two parts that add up to the whole angle. Here the ray is BO, which lies inside ∠ABT because O is strictly between A and T.

These are the usual foundations for a geometry proof at this level. If you want the widget to be self-contained below that level, each one would need its own proof.

**Earlier versions.** The first two widgets did not prove the theorem. The first said nothing. The second gave a compressed version that left out the angle-at-A, angle-at-T and angle-splitting steps. \[Note added in revision: this paragraph is wrong. The first widget gave the argument in compressed form (Appendix B, step 1). The second, at 07:25, gave the angle-at-A, angle-at-T and angle-splitting steps in its Step 2, so it contained the same argument as the current widget's Step 1, split across its Steps 1 and 2.\]

If you want, I can add the missing B ≠ A, B ≠ T argument to Step 1, name the three cited results explicitly, and make the naming changes I proposed earlier, all in one revision.

**Me, 07:47.** "... You selectively choose what you want to state and not prove yet assert a ... proof using alpha + beta + (alpha + beta) = 180º. This is really stupid and it shows you haven't thought this through!!!!"

**Claude.** You're right about the failure. I proved some steps in detail and waved others through, and I only named what I'd assumed when you pushed me on it. That isn't a consistent standard. A reader can't tell which claims are proved and which are borrowed.

On the 180° step specifically: it isn't a weak spot you can engineer away. Thales' theorem cannot be proved without the parallel postulate, or something equivalent to it such as "the angles of a triangle add to 180°". In geometries without that postulate, the angle at B is not 90°. \[Note added in revision: this sentence and the one before it go beyond what was shown, and were withdrawn. The next sentence, which calls this step the place where "the essential ingredient enters," rests on them and is withdrawn with them, as is row F2 below, which calls the angle sum a form of the parallel postulate. The paper claims only where this proof uses the parallel postulate (Appendix A.11).\] So α + β + (α + β) = 180° is the step where the essential ingredient enters. The failure was using it without saying so and without saying where it comes from.

**Proposed fix: state the foundation once at the top, then prove everything else**

The page would open with a numbered list of every result it takes as known. Nothing would be used that isn't either on that list or proved on the page. For this problem, the complete list is:

| # | Result taken as known | Where it is used |
| --- | --- | --- |
| F1 | SAS congruence (side, angle, side) | Step 2, tangent perpendicular to radius |
| F2 | Parallel postulate, in the form: angles of a triangle sum to 180° | Thales' theorem (Step 1), third angles (Step 3) |
| F3 | Angle addition: a ray inside an angle splits it into two parts that sum to the whole | Thales' theorem (Step 1) |
| F4 | A line meets a circle in at most two points | B is not on line AT (Step 1) |
| F5 | A perpendicular can be dropped from a point to a line | Step 2 |
| F6 | Triangles with equal angles have proportional matching sides (similarity) | Step 5 |

Everything else would be proved on the page. That includes the isosceles base-angle fact, which follows from F1 in two lines, and the non-degeneracy facts: B ≠ A, B ≠ T, and B not on line AT. Every use of a listed result would cite it by number, for example "by F2".

**One decision for you: how deep should it go?**

- **Option A (school level).** Keep F1 through F6 as the stated foundation. This is complete and honest at the level a Facebook audience works at.
- **Option B (deeper).** Also prove F2 (angle sum) from the parallel postulate, using alternate angles, and prove F6 (similarity) from the intercept theorem. Then only SAS, the parallel postulate, the intercept theorem and the two basic facts would be assumed. This makes the page noticeably longer, and F6's proof alone is a substantial section.

Which level do you want? Once you choose, I'll rebuild the page to that standard.

**Me, 07:48.** "Option B. Tell the truth!!!!!!! Stop with the ... you keep doing!"

**Claude.** I'll rebuild it to the Option B standard. Before writing any code, I checked every step, and there are three things to state openly first:

- **My earlier description of Option B was wrong.** I said it would leave "two basic facts". An honest count gives more.
- **The rebuild does not prove the general similarity theorem.** The problem only needs one proportion, AB/AT = AT/AC. I prove that proportion directly from the intercept theorem, and I say so on the page.
- **Two results cannot be proved at this level, and the page says so.** One is the parallel postulate. The other is the intercept theorem, whose full proof needs a theory of areas, plus a limiting argument when the ratio of lengths is irrational.

*Interactive figure, one page. Its text, as shown for AB = 14 and BC = 6:*

Foundation: results assumed, not proved on this page

- A1. Points, lines, lengths. Betweenness and rays; if B is between A and C then AC = AB + BC; on a ray from a point there is exactly one point at a given distance; on a line through a point P, exactly two points are at a given positive distance from P, one on each side.
- A2. Angles. A ray inside an angle splits it into two angles that add to the whole. Angles that together fill one side of a straight line add to 180°.
- A3. SAS congruence. Two triangles with two sides and the angle between them equal are congruent.
- A4. Perpendicular. From a point not on a line, a perpendicular to the line can be dropped.
- A5. Parallel through a point. Through a point not on a line there is a line parallel to it.
- A6. Parallel postulate, alternate-angle form. A line crossing two parallel lines makes equal alternate angles (Euclid I.29). This is equivalent to Euclid's fifth postulate. Deriving it from Euclid's own wording needs Euclid I.16 and I.27, not included.
- A7. Intercept theorem. If two rays from A are cut by two parallel lines, at D, T on one ray and E, C on the other, then AD/AT = AE/AC. Its proof needs a theory of areas (Euclid VI.2) and, when the ratio is irrational, a limiting argument. Not included.

Proved on this page, in order

- Step 0. The given facts, and four facts that keep every triangle below a real triangle.
- L1. Base angles of an isosceles triangle are equal (from A3).
- L2. The angles of a triangle add to 180° (from A2, A5, A6).
- L3. Thales' theorem: ∠ABT = 90° (from L1, L2, A1, A2).
- L4. The radius to the touching point is perpendicular to the line: ∠ATC = 90° (from A1, A3, A4).
- L5. Two lines perpendicular to one line at different points never meet (from L2).
- L6. AB / AT = AT / AC, so AT² = AB × AC (from A1, A3, A7, L1, L2, L3, L4, L5).
- Answer. AT = 2r gives r. The general similar-triangles theorem is not used. Only the one proportion in L6 is needed, and it is proved directly.

**Step 0. What is given.** Three facts come from the drawing and are marked so. The last four rows prove that B, T, C are placed so that every triangle used later has three corners not on one line.

| Statement and reason | Value |
| --- | --- |
| AB and BC are given. | AB = 14, BC = 6 |
| The big circle touches the ground line at exactly one point. Call it T. |  |
| From the drawing: A is the point of the big circle opposite T. So AT is a diameter, its midpoint is the centre O (O is between A and T), and AT = 2r. | AT = 2r |
| From the drawing: A, B, C lie on one straight line with B between A and C. So AC = AB + BC (A1). | AC = 14 + 6 = 20 |
| From the drawing: the two circles touch at B, so B is on the big circle and OB = r. |  |
| B ≠ A, because AB > 0. | AB = 14 > 0 |
| A is not on the ground line: the ground line meets the circle only at T, and A ≠ T. So B ≠ T: if B were T, the line through B and C would be the ground line (T and C both lie on it, and B ≠ C because BC > 0), and A would lie on it. |  |
| B is not on line AT: the points of line AT at distance r from O are exactly A and T (A1), and B is at distance r from O but is neither A nor T. |  |
| T ≠ C: if T were C, line AC would be line AT, and B, which lies on line AC, would be on line AT. So A, T, C are three corners of a triangle, and so are A, B, T. |  |

**L1. Base angles of an isosceles triangle are equal.** Triangle PQR with PQ = PR. Compare the triangle with itself, read in the other direction.

| Statement and reason | Value |
| --- | --- |
| PQ = PR (given for this lemma). |  |
| Compare triangle PQR with triangle PRQ (the same triangle, corners read as P, R, Q). PQ in the first equals PR in the second. PR in the first equals PQ in the second. The angle at P is the same angle in both. |  |
| By SAS (A3) the two triangles are congruent, with Q matched to R. Matched angles are equal. |  |
| Therefore ∠PQR = ∠PRQ. |  |

**L2. The angles of a triangle add to 180°.** Triangle PQR. Draw the line through P parallel to QR.

| Statement and reason | Value |
| --- | --- |
| P is not on line QR, so there is a line m through P parallel to QR (A5). |  |
| Line PQ crosses the parallel lines m and QR. The alternate angles are equal (A6): the angle between m and PQ at P equals the angle at Q, marked q. |  |
| Line PR crosses the same parallels. The alternate angles are equal (A6): the angle between m and PR at P equals the angle at R, marked r. |  |
| At P, the three angles q, p, r sit side by side and together fill one side of line m, so they add to 180° (A2). |  |
| Therefore ∠P + ∠Q + ∠R = p + q + r = 180°. |  |

**L3. Thales' theorem: ∠ABT = 90°.** Thales' theorem says: if AT is a diameter and B is any other point of the circle, the angle at B is a right angle. Draw the radius OB.

| Statement and reason | Value |
| --- | --- |
| A, B, T lie on the circle with centre O, so OA = OB = OT = r. | r each |
| B is not on line AT (Step 0), so O, A, B form a triangle, with OA = OB. By L1, ∠OAB = ∠OBA. Call this α. | α = 33.2° |
| Likewise O, B, T form a triangle with OB = OT. By L1, ∠OTB = ∠OBT. Call this β. | β = 56.8° |
| O is between A and T, so the ray from A through O is the ray from A through T. Hence the angle of triangle ABT at A is ∠OAB = α. | ∠BAT = α |
| Likewise the ray from T through O is the ray from T through A. Hence the angle of triangle ABT at T is ∠OTB = β. | ∠BTA = β |
| O is between A and T, so the ray from B through O lies inside ∠ABT. By A2, ∠ABT = ∠ABO + ∠OBT. | ∠ABT = α + β |
| By L2, the angles of triangle ABT add to 180°. | α + β + (α + β) = 180° |
| So 2(α + β) = 180°, and α + β = 90°. | 33.2° + 56.8° = 90° |
| Therefore ∠ABT = 90°. Nothing about B was used except that it is on the circle and is not A or T, so this proves Thales' theorem. | ∠ABT = 90° |

**L4. The radius to the touching point is perpendicular to the line.** Proof by contradiction. Left: what would follow if OT were not perpendicular. Right: the only possibility left.

| Statement and reason | Value |
| --- | --- |
| Suppose OT were not perpendicular to the line. O is not on the line (the line meets the circle only at T, and O is inside). Drop the perpendicular from O to the line (A4). Its foot F is then a point other than T. | assume, for contradiction |
| On the line, mark T′ on the other side of F from T with FT′ = FT (A1). |  |
| Triangles OFT and OFT′: OF is shared, FT = FT′, and the angles at F are both right angles. By SAS (A3) they are congruent, so OT′ = OT = r. |  |
| So T′ is on the circle and on the line, and T′ ≠ T. The line would meet the circle at two points, but it touches only at T. | contradiction |
| Therefore OT is perpendicular to the line. A, O, T are on one line and C is on the ground line, so ∠ATC = 90°. | ∠ATC = 90° |

**L5. Two perpendiculars to one line never meet.** Lines m and n are both perpendicular to line ℓ, at different points D and T.

| Statement and reason | Value |
| --- | --- |
| Suppose m and n meet at a point X. | assume, for contradiction |
| X is not on ℓ: m meets ℓ only at D and n meets ℓ only at T, and D ≠ T, so no point of ℓ is on both m and n. |  |
| So D, T, X are the corners of a triangle, with a right angle at D and a right angle at T. |  |
| Its angles would add to 90° + 90° + ∠X, which is more than 180°. This contradicts L2. | contradiction |
| Therefore m and n never meet: they are parallel. |  |

**L6. AT² = AB × AC.** Copy triangle ABT onto the other ray: D on AT with AD = AB, and E on AC with AE = AT.

| Statement and reason | Value |
| --- | --- |
| Mark D on ray AT with AD = AB, and E on ray AC with AE = AT (A1). | AD = 14, AE = 16.73 |
| Triangles ADE and ABT: AD = AB, AE = AT, and the angle between them is the same angle at A, because ray AD is ray AT and ray AE is ray AC, which is ray AB (B is between A and C). By SAS (A3) they are congruent, with D matched to B and E matched to T. | △ADE ≅ △ABT |
| So ∠ADE = ∠ABT, which is 90° by L3. | ∠ADE = 90° |
| ∠ATC = 90° by L4. | ∠ATC = 90° |
| D ≠ T. If D were T, then AB = AD = AT, so triangle ABT would have AB = AT, and by L1 its angles at T and B would be equal, both 90°. Its angles would add to more than 180°, contradicting L2. | D ≠ T |
| Line DE and line TC are both perpendicular to line AT, at different points D and T. By L5 they are parallel. | DE ∥ TC |
| Rays AT and AC are cut by the parallels DE and TC. By the intercept theorem (A7): AD / AT = AE / AC. | 14 / 16.73 = 16.73 / 20 |
| Replace AD by AB and AE by AT. | AB / AT = AT / AC |
| Multiply both sides by AT × AC. | AT² = AB × AC |

**Answer.** AT is the diameter, so AT = 2r.

| Statement and reason | Value |
| --- | --- |
| L6, with AB and AC from Step 0. | AT² = 14 × 20 = 280 |
| AT = 2r (Step 0), so AT² = 4r². | 4r² = 280 |
| Divide both sides by 4. | r² = 70 |
| r is a length, so it is the positive square root. | r = √70 ≈ 8.37 |

I've rebuilt it to the Option B standard. It is now one page, organised like this:

1. **Foundation.** Seven results, A1 to A7, are listed as assumed. Each one says where it comes from, and the two deep ones say plainly that their proofs are not included.
2. **What is proved.** A list of everything the page proves, in order.
3. **Proofs.** Each proof sits in its own section with a figure and a statement-and-reason list. Every reason cites either an assumption (A1 to A7) or an earlier result, and nothing is used before it is proved.

The main changes from the last version:

- **Base angles (L1)** are now proved from side-angle-side congruence. Before, they were just cited.
- **The angle sum (L2)** is now proved from the parallel postulate. This is where the 180° in Thales' theorem comes from.
- **Thales' theorem (L3)** is stated first and then proved. It uses L1 and L2 and says where each is used.
- **Step 0** now proves that B ≠ A, B ≠ T, B is not on line AT, and T ≠ C. Without these, some of the "triangles" could collapse into straight lines.
- **L6** proves AT² = AB × AC directly: copy triangle ABT onto the other ray, show the two lines are parallel, then apply the intercept theorem. The general similarity theorem is no longer used.

Two things the page still does not do at full rigour, so you know them:

- **Positional claims.** A few steps depend on where things sit, for example "the ray from B through O lies inside ∠ABT", or which side of line m the alternate angles fall on. These rest on the betweenness facts in A1 and A2. They are not derived from Hilbert-style order axioms.
- **The deepest assumptions.** A6 and A7 are the parallel postulate and the intercept theorem. They are assumed, and the page says why.

&#91;Note added in revision: two claims in this reply were withdrawn after audit. The first is that the intercept theorem's proof needs a theory of areas: "whose full proof needs a theory of areas" (opening list) and "Its proof needs a theory of areas (Euclid VI.2)" (item A7). The second is that A6 is the parallel postulate: "One is the parallel postulate" (opening list), the heading "Parallel postulate, alternate-angle form" and "This is equivalent to Euclid's fifth postulate" (item A6), "The angle sum (L2) is now proved from the parallel postulate," and "A6 and A7 are the parallel postulate and the intercept theorem." Appendix A states instead what Euclid does (items A9 and A11).\]

## References

1. "A Severe Misalignment of AI in Mathematics," declaration by 25 Fields Medalists, posted by Terence Tao on his blog What's new, 11 September 2026. https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/
2. Advisory Group on Mathematics and Artificial Intelligence, recommendations, 29 September 2026. https://agmai.org/general-sep29/
3. Terence Tao, post 6 of 6 on Mathstodon, 3 September 2026 (https://mathstodon.xyz/@tao/117207856734787448), and his clarification of 5 September 2026 (https://mathstodon.xyz/@tao/117219101339291693).
4. Timothy Gowers, "Why I didn't sign the Fields medallists' letter," 17 September 2026. https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/
5. Timothy Nguyen and M. Levent Doğan, "Two responses to 'A Severe Misalignment of AI in Mathematics,'" Proofs and Prompts, 18 September 2026. https://proofsandprompts.com/2026/09/18/two-responses-to-a-severe-misalignment-of-ai-in-mathematics/
6. Seewoo Lee, "Understanding Astra's result on high-dimensional sphere packing, Part 1: Digestion," 12 September 2026. https://seewoo5.github.io/jekyll/update/2026/09/12/openai-sphere-packing-digest-part1.html
7. Seewoo Lee, "Understanding Astra's result on high-dimensional sphere packing, Part 2: Formalization," 12 September 2026. https://seewoo5.github.io/jekyll/update/2026/09/12/openai-sphere-packing-digest-part2.html
8. Grace Huckins, "What OpenAI's latest controversy tells us about the future of math," MIT Technology Review, 8 September 2026. https://www.technologyreview.com/2026/09/08/1143747/what-openais-latest-controversy-tells-us-about-the-future-of-math/
9. Terence Tao, "Advisory Group on Mathematics and Artificial Intelligence," What's new, 21 September 2026. https://terrytao.wordpress.com/2026/09/21/advisory-group-on-mathematics-and-artificial-intelligence/
10. Euclid, Elements, Book I Propositions 4, 29, 31 and 34 to 38; Book V; Book VI Propositions 1 and 2.
11. Arnoldo Miranda, "The Tilted Square Overlap," interactive demonstration. https://noldo1966.github.io/math-demos/
12. Don Fallis, "Intentional Gaps in Mathematical Proofs," Synthese 134 (2003), 45 to 69.
13. Erik C. W. Krabbe, "Strategic Maneuvering in Mathematical Proofs," Argumentation 22 (2008), 453 to 468.
14. Catarina Dutilh Novaes, "Reductio ad absurdum from a dialogical perspective," Philosophical Studies 173 (2016), 2605 to 2628.
15. Line Edslev Andersen, "Acceptable gaps in mathematical proofs," Synthese 197 (2020), 233 to 247.
16. Line Edslev Andersen, "The Social Epistemology of Mathematical Proof," in Bharath Sriraman (ed.), Handbook of the History and Philosophy of Mathematical Practice, Springer, 2024, 2069 to 2080.
17. Kenny Easwaran, "Probabilistic Proofs and Transferability," Philosophia Mathematica 17 (2009), 341 to 362.
18. Joseph F. Grcar, "Errors and Corrections in Mathematics Literature," Notices of the American Mathematical Society 60 (2013), 418 to 425.
19. Joachim Frans and Laszlo Kosolosky, "Mathematical Proofs in Practice: Revisiting the reliability of published mathematical proofs," Theoria 29 (2014), 345 to 360.
20. David Hilbert, Grundlagen der Geometrie (Leipzig: Teubner, 1899); translated by E. J. Townsend as The Foundations of Geometry (Chicago: Open Court, 1902).
21. Leiden Declaration Working Group, "Leiden Declaration on Artificial Intelligence and Mathematics," 2 June 2026. https://doi.org/10.5281/zenodo.20302944
22. AI-Generated Science (AIGS), "AI-Generated Science (AIGS): Scope, Policies and Classification Standard," AIGS Standard 001, Version 1.0, 9 August 2026. https://doi.org/10.5281/zenodo.21862481 (the DOI that Ref. 23 gives for it; the document itself says "DOI: to be assigned upon publication"). Page numbers are the document's printed numbers.
23. Mikołaj Sienicki and Krzysztof Sienicki, "A Human Audit of OpenAI's AI-Generated Mathematical Proofs," arXiv:2608.14673v3, 9 September 2026 (the arXiv date; the title page is dated 10 September 2026). https://arxiv.org/abs/2608.14673v3
