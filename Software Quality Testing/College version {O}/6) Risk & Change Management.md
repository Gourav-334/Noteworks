# $\fbox{Chapter 6: RISK \& CHANGE MANAGEMENT}$





## **Topic - 1: Software Risks**

### <u>Categories</u>  

#### Project risks:

- Schedule slippage
- Cost increase
- Budget/ staff/ resource/ customer/ requirement issues

#### Technical risks:

- Affect quality & timeliness
- Include design
- Implementation
- Interface
- Verification
- Maintenance
- Specification ambiguity
- Uncertainty
- Obsolescence
- Leading-edge tech

#### Business risks:

- Threatens product viability.
  1. **Market risk $\rightarrow$** Product nobody wants.
  2. **Strategic risk $\rightarrow$** Product misaligned with company strategy.
  3. **Sales risk $\rightarrow$** Sales team unable to sell.
  4. **Management risk $\rightarrow$** Loss of senior management support.
  5. **Budget risk $\rightarrow$** Loss of funding or resources.

#### Predictable risks:

- From past experience
- Staff turnover
- Poor customer communication

#### Unpredictable risks:

- Hard to foresee
- Random disruptions



## **Topic - 2: Risk Identification**

### <u>Introduction</u>

- Systematic attempt to specify threats to project plan (cost, schedule, resources).
- Product-specific risks are identified by those with knowledge of technology & environment.
- While generic risks are common to all projects.


### <u>Key Risk Factors</u>  

- **Business impact $\rightarrow$** Management / market constraints.
- **Customer characteristics $\rightarrow$** Communication & customer sophistication.
- **Product size $\rightarrow$** Larger software means higher risk.
- **Process definition $\rightarrow$** Clarity & adherence of development process.
- **Development environment $\rightarrow$** Availability / quality of tools.
- **Technology complexity $\rightarrow$** Newness and difficulty of system.
- **Staff size & experience $\rightarrow$** Skills and experience level of engineers.



## **Topic - 3: Risk Projection (Estimation)**  

### <u>Introduction</u>

- Probability ($P$) → Likelihood risk occurs
- Consequence ($C$) → Impact if it occurs
- Risk Exposure ($RE$) = $P \times C$


### <u>Steps</u>  

1. Estimate probability of occurrence  
2. Estimate impact using defined criteria  
3. Complete risk table and analyze  



## **Topic - 4: Risk Refinement, Mitigation, Monitoring & Management (RMMM)**  

### <u>Introduction</u>

- Risks refined into more detailed ones for handling.
- Goal is to develop effective risk-handling strategy.


### <u>Strategies</u>  

- **Risk avoidance $\rightarrow$** Proactive planning to prevent.
- **Risk monitoring $\rightarrow$** Track occurrence, apply aversion steps, collect data.
- **Risk management/contingency $\rightarrow$** Handle if risk materializes.


### <u>RMMM Plan</u>  

- Document describing all risk analysis activities.
- Each risk documented in **risk information sheet (RIS)**.
- After project starts, mitigation & monitoring commence.

#### Risk monitoring objectives:

  1. Check if predicted risks occur.
  2. Ensure avoidance steps applied.
  3. Gather info for future analysis.



## **Topic - 5: Software Configuration Management (SCM)**

### <u>Introduction</u>

- Activities to control change.
- Identify work products likely to change.
- Define version control mechanisms.
- Manage imposed changes.
- Audit & report changes.


### <u>Origins of Change</u>  

- New market / business conditions
- New customer needs
- Reorganization or scaling
- Budget / schedule constraints



## **Topic - 6: Baselines**

- **<u>IEEE 610.12-1990</u>:** Specification/product reviewed & agreed upon, becomes basis for further development, modifiable only via formal change control.



## **Topic - 7: Software Configuration Items (SCI)**

- **<u>SCI</u>:** Information created during software engineering.
- Each config object has name, attributes, relations.
- Examples: design spec, data model, components, source code, test specs, etc.



## **Topic - 8: Change Control**

- Formal process to manage modifications.
- Typically represented as **change control process (CCP)** diagram.

```css
/* Diagram Placeholder: Change Control Process */
```



## **Topic - 9: Configuration Audit**  

### <u>Introduction</u>

- Ensures change properly implemented.
- Complements technical review.


### <u>Questions</u>  

- Was ECO change made? Any extra modifications?
- Was technical review conducted?
- Was process followed & standards applied?
- Are changes documented with date / author in SCI?



## **Topic - 10: SCM for Web Applications**

### <u>Challenges</u>  

- **Object diversity $\rightarrow$** HTML, CSS, JS, media, templates, applets, scripts.
- **Tool compatibility $\rightarrow$** Must support varied file types & editors.
- **Mixed objects $\rightarrow$** Same file can contain multiple object types (HTML+CSS+JS).
- **Developers $\rightarrow$** Engineers & non-technical users. Interface must be accessible.
- **Rate of change $\rightarrow$** Web apps evolve faster, need fine-grained tracking.


### <u>SCM Tools for Web</u>  

- *GitLab*, *SourceForge*, *Cloud Source Repositories*, *GitKraken*, *Apache Allura*.
- **Configuration & automation tools $\rightarrow$** *SolarWinds*, *CFEngine*, *Puppet*, *Chef*, *Ansible*, *SaltStack Juju*.

---
