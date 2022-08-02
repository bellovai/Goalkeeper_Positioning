# Goalkeeper_Positioning
GitHub repository for my master's thesis.

## Next steps
### Done
- Create and share GitHub repository
- Create and share LaTeX template
- Create and share group library on Zotero
- Isolate 1v1 situations (including misses)
- Define "theoretical optimal goalkeeper position" in code
- Define "theoretical optimal goalkeeper position" in words
- Explore goalkeeper positioning literature: TOGKP models, positioning rules, goalkeeper reach, reaction time
- Plot deviations from goalkeeper position to TOGKP
### To do
- Plot deviations from goalkeeper position to average goalkeeper position
- Improve TOGKP model: forward dive, reaction time

## Ideas
### Goalkeeper positioning analysis
- Impact of goalkeeper height to goalkeeper positioning
- Goalkeeper positioning patterns in various situations (1v1s, shots from different „zones", shots with a crowded penalty area)
- Train goalkeeper positioning improvements: visualize shooting cone
### ML part: compare different TOGKP models
##### TOGKP models (which models to include, write models, code models)
- Bisector model: The TOGKP lies on the shooting-angle's bisector, as far out of the goal for the "goalkeeper reach“ to cover the whole shooting angle.
- Goalcenter model: Same as "bisector model" but the shooting-angle's bisector is replaced with the line connecting the ball with the goalcenter.
- Nearest neighbor model: For each shot, the TOGKP is the average goalkeeper position of the 20 most similar shots.
- Minimal xG model: Train an xG model including the real goalkeeper position as a feature. In testing, the TOGKP is the position that results in the lowest xG value.
- Zone model: TOKGP model from "Analytic method for evaluating players’ decisions in team sports: Applications to the soccer goalkeeper".
##### Evaluation metrics
- Compare average distance from TOGKP to goalkeeper position for goals and no-goals (for different zones)
- Compare average distance from TOGKP to average goalkeeper position and goalkeeper position
- Compare average xG value for TOGKP and goalkeeper position
### Descriptive part: reexpression of cartesian coordinates
- Effect on learning algorithms
- Easy to understand scatter plots (goal at the bottom)
- Plot two data points agains each other
- Divide pitch into zones

## Keep in mind
- Consider existing work, logically explain relations to existing work, reason choices, create defensible work
- Create properly written thesis, people unfamiliar with the topic need to understand the thesis / outcome

## Later
- All shots on one side (symetric)
- Improve 1v1 dataset: exclude 2v1, exclude side shots, control manually
- Look at goalkeepers individually
- Gender differences: female goalkeepers further out of the goal because of smaller goalkeeper reach
- Image recognition of diving styles
