# Patrol Effort Plot Workflow

## Introduction

This workflow helps you to track how your patrol effort and patrol results change over time. It turns **EarthRanger** patrol data into a single interactive chart of the patrol metrics you choose — as bars or lines, summarized by week, month, or any other time interval.

**What this workflow does:**
- Downloads patrols and the events reported during those patrols from **EarthRanger**
- Calculates patrol metrics such as patrol count, patrol days, distance covered, time on patrol, event counts, and encounter rates
- Summarizes each metric over a time interval you choose (year, month, week, day, or hour)
- Optionally splits a metric into separate series by category (e.g. event type), by spatial region, or across time periods (e.g. compare this month against last month)
- Creates an interactive bar or line chart on a dashboard, styled with your choice of colors

**Who should use this:**
- Conservation managers monitoring patrol effort and coverage
- Researchers analyzing trends in patrol activity and wildlife encounters
- Anyone needing to visualize how patrol metrics stored in EarthRanger change over time

## Prerequisites

Before using this workflow, you need:

1. **Ecoscope Desktop** installed on your computer
   - If you haven't installed it yet, please follow the installation instructions for Ecoscope Desktop

2. **EarthRanger Data Source** configured in Ecoscope Desktop
   - You must have already set up a connection to your EarthRanger server
   - Your data source should be configured with proper authentication credentials
   - You'll need to know the name of your configured data source (e.g., "mep_dev")

3. **Patrols recorded in EarthRanger**
   - Your EarthRanger site should contain patrols (with tracked patrol segments) for the time period you want to analyze
   - If you want to analyze specific patrol types, you can find their names in your EarthRanger Admin site under **Activity → Patrol Types**
   - If you plan to split the chart by spatial region, you also need a **Spatial Feature Group** set up in EarthRanger (**Mapping → Spatial Feature Group Profiles**)

## Installation

1. Select "Workflow Templates" tab
2. Click "+ Add Template"
3. Copy and paste this URL https://github.com/wildlife-dynamics/patrol-effort-plot and wait for the workflow template to be downloaded and initialized
4. The template will now appear in your available template list

## Configuration Guide

### Basic Configuration

#### 1. Workflow Details
Give your workflow run a recognizable identity.

- **Name** (required): A name for this analysis
  - Example: `Patrol Effort Plot`
- **Description** (optional): A short note on what this run covers
  - Example: `Patrol metric trends over time as a bar chart.`

#### 2. Data Source
Select the EarthRanger connection to pull data from.

- **Data Source** (required): The name of your configured EarthRanger data source
  - Example: `mep_dev`

#### 3. Time Range
Set the period to analyze.

- **Since** (required): Start of the analysis period
  - Example: `2015-01-10T00:00:00`
- **Until** (required): End of the analysis period
  - Example: `2015-02-28T23:59:59`
- **Timezone** (required): The timezone used to interpret and display times
  - Example: `UTC (UTC+00:00)` or `Africa/Nairobi (UTC+03:00)`

#### 4. Patrol and Event Types
Choose which patrols and events to include.

- **Patrol Types** (optional): The patrol type(s) to analyze. Leave empty to analyze all patrol types.
  - Example: `demo_patrol`
  - Note: If you are on Ecoscope Desktop, "Patrol Type" values can be found in your EarthRanger Admin site under **Activity → Patrol Types**
- **Event Types** (optional): The event type(s) to count. Enter the "Event Types" value for each event type — one per field (e.g. `wildlife_sighting_rep`). Leave empty to count all patrol events.
- **Status** (optional): Which patrol statuses to include
  - Default: `Done`
  - Options: Scheduled, Active, Overdue, Done, Cancelled

#### 5. Filter Data
Optionally restrict the data by location or movement characteristics. Most users can leave this section at its defaults.

- **Bounding Box** (optional): Only include patrol observations and events inside this rectangle (west/south/east/north coordinates)
- **Filter Exact Point Coordinates** (optional): Exclude observations recorded at these exact coordinates (e.g. known default GPS points)
- **Trajectory Segment Filter** (optional): Limits on segment speed, duration, and distance used when building patrol tracks — useful for removing GPS noise

#### 6. Group Data
Optionally split the results into separate dashboard views — one chart per group.

- **Groupers** (optional): Add one or more groupings:
  - **Category**: Split by `Patrol Serial Number`, `Patrol Type`, or `Patrol Subject`
  - **Temporal**: Split by time period, e.g. `%Y` (Year), `%B` (Month), `%Y-%m-%d` (Date)
  - **Spatial**: Split by the regions of an EarthRanger spatial feature group
  - Note: Leave empty to produce a single chart for the whole time range

#### 7. Trend Chart
The heart of the workflow: pick the metrics, the time interval, and what each series represents.

- **Metrics** (required): Add one or more metric rows. Each metric becomes one series on the chart (default: `Patrol Count`). Available metrics:
  - **Patrol Count**: Number of patrols
  - **Patrol Days**: Number of distinct days with patrol movement
  - **Total Distance** / **Total Duration**: Distance covered / time spent on patrol (with a unit of your choice)
  - **Total Events**: Number of events reported during patrols
  - **Total Encounters**: Sum of a numeric event field (set **Aggregate Column** to the event field to sum, e.g. `number_of_animals`); without a column it counts events
  - **Encounters per Distance** / **per Duration** / **per Patrol** / **per Patrol Day**: Encounter rates relative to patrol effort
  - **Area Covered (Merged / Unmerged)**: Area swept by patrols given a swath width
  - **Custom**: Your own aggregation over any data column
- **Time Interval** (required): The time bucket for the x-axis — how metrics are summarized over time
  - Default: `Week`
  - Options: Year, Month, Week, Day, Hour
- **Compares** (required): What each series represents
  - Default: `Metrics Only`
  - **Metrics Only**: One series per metric row
  - **Category**: The single metric split into one series per category value — choose the **Category**: `Event Type`, `Patrol Type`, `Patrol Subject`, or `Patrol Serial Number`
  - **Spatial Group**: The single metric split into one series per region — enter the **Spatial Feature Group** name exactly as it appears in your EarthRanger site (**Mapping → Spatial Feature Group Profiles**)
  - **Time**: The single metric compared across periods — choose the **Period** (Years, Months, Weeks, or Days). One series per period, overlaid on a shared axis.
  - Note: When comparing by Category, Spatial Group, or Time, keep exactly **one** metric row — the form will not submit multiple metrics with a breakdown
  - Note: For the Time comparison, the Time Interval must be smaller than the Period — e.g. a `Month` interval to compare `Years`

#### 8. Styling
Control how the chart looks.

- **Chart Type** (required): Render the trend as `Bar` or `Line` (default: `Bar`)
- For **Bar** charts:
  - **Bar Mode**: `Grouped` shows series side by side; `Stacked` piles them up (best when all series share a unit). Default: `Grouped`
  - **Show value labels on each bar**: Print the value on top of each bar (default: on)
- For **Line** charts:
  - **Line Shape**: Straight or smooth (spline) lines
  - **Line Style**: Solid, dashed, or dotted
  - **Mark each data point on the line**: Show point markers (default: on)
- **Color Palette**: Either a named **Color Map** (default: `Tab20b`; also Tab10, Tab20, Set2, Dark2, Paired, Viridis, Plasma) or **Custom Colors** — a list of hex colors (e.g. `#123456`) cycled over the series
- **Y-Axis Title** (optional): A label for the value axis, e.g. `Count`. Leave empty for no label.

## Running the Workflow

Once you've configured all the settings:

1. **Review your configuration**
   - Double-check your time range, data source, and patrol types

2. **Save and run**
   - Click the "Submit" and the workflow will show up in "My Workflows" table button in Ecoscope Desktop
   - Click on "Run" and the workflow will begin processing

3. **Monitor progress and wait for completion**
   - You'll see status updates as the workflow runs
   - Processing time depends on:
     - The size of your date range
     - Number of patrols and patrol events in the period
     - Whether spatial regions need to be fetched and matched
   - The workflow completes with status "Success" or "Failed"

## Understanding Your Results

After the workflow completes successfully, open the run to view its dashboard.

### Visual Outputs (Dashboard)

The workflow creates an interactive dashboard with one main visualization:

#### Patrol Effort Plot
- **Format**: Interactive bar or line chart (per your Styling choices)
- **Features**:
  - X-axis: Time, bucketed by your chosen Time Interval (or "Week 1..N" within each period when comparing by Time)
  - Y-axis: The metric value(s), labeled with your Y-Axis Title if set
  - One series per metric — or per category value, spatial region, or time period when a comparison is chosen
  - Legend: Always shown, naming each series (e.g. `Total Events`, `Wildlife Sighting`, or `Jan 2015`)
  - Interactive hover: Shows exact values when you mouse over bars or points
  - Value labels: Printed on bars when enabled in Styling

If you configured **Group Data** groupers, the dashboard gains a view selector — one chart per group (e.g. one per month, or one per patrol type).

Note: encounter-rate metrics are labeled automatically — e.g. `Events per Patrol Day`, or `Number Of Animals per km` when an Aggregate Column is set.

## Common Use Cases & Examples

Here are some typical scenarios and how to configure the workflow for each:

### Example 1: Weekly patrol activity at a glance
**Goal**: See how many patrols ran each week.

**Configuration**:
- **Time Range**:
  - Since: `2015-01-10T00:00:00`
  - Until: `2015-02-28T23:59:59`
  - Timezone: `UTC (UTC+00:00)`
- **Patrol Types**: `demo_patrol`
- **Trend Chart**: Metrics: `Patrol Count`; Time Interval: `Week`; Compares: `Metrics Only`
- **Styling**: Chart Type `Bar`, Bar Mode `Grouped`, Color Map `Tab20b`

**Result**:
- A weekly bar chart of patrol counts across the whole period — the workflow's default setup, submitted as-is

---

### Example 2: What kinds of events do patrols encounter?
**Goal**: Break monthly patrol events down by event type.

**Configuration**:
- **Time Range**: as above
- **Trend Chart**: Metrics: `Total Events`; Time Interval: `Month`; Compares: `Category` with Category `Event Type`
- **Styling**: Chart Type `Bar`, Bar Mode `Stacked`, value labels off

**Result**:
- One stacked bar per month, with a colored segment per event type (using the readable event type names from EarthRanger, e.g. "Wildlife Sighting")

---

### Example 3: Compare patrol effort across regions
**Goal**: See which sectors get the most patrol coverage.

**Configuration**:
- **Time Range**: as above
- **Trend Chart**: Metrics: `Patrol Count`; Time Interval: `Month`; Compares: `Spatial Group` with your feature group name (e.g. `SpatialGrouperTest`)

**Result**:
- One series per region in the feature group (e.g. Central / East / West), showing monthly patrol counts side by side

---

### Example 4: Is this month better than last month?
**Goal**: Compare weekly patrol counts across months.

**Configuration**:
- **Time Range**: as above
- **Trend Chart**: Metrics: `Patrol Count`; Time Interval: `Week`; Compares: `Time` with Period `Months`
- **Styling**: Chart Type `Line`

**Result**:
- One line per month plotted over a shared "Week 1, Week 2, …" axis, so the same week of each month lines up for direct comparison

---

### Example 5: Wildlife counted per kilometer patrolled
**Goal**: Track animals seen relative to patrol effort.

**Configuration**:
- **Time Range**: as above
- **Trend Chart**:
  - Metrics: `Total Encounters` with Aggregate Column `number_of_animals`, and `Encounters per Distance` with unit `km` and the same Aggregate Column
  - Time Interval: `Month`; Compares: `Metrics Only`

**Result**:
- Monthly bars for total animals recorded and animals per kilometer, labeled `Total Number Of Animals` and `Number Of Animals per km`

## Troubleshooting

### Common Issues and Solutions

#### Workflow fails to start
**Problem**: The workflow fails immediately with a connection or authentication error.

**Solutions**:
- Verify your EarthRanger data source is configured correctly in Ecoscope Desktop
- Check that your username and password are still valid on the EarthRanger site
- Confirm you can reach your EarthRanger server from your network

#### The chart is empty or the run reports no data
**Problem**: The workflow succeeds but the chart shows no bars or lines.

**Solutions**:
- Widen your time range — there may be no patrols in the selected period
- Check the patrol **Status** filter: by default only `Done` patrols are included
- Verify the patrol type names match your EarthRanger Admin site (**Activity → Patrol Types**) exactly
- If you set Event Types, confirm the values match the "Event Types" values in EarthRanger (e.g. `wildlife_sighting_rep`)
- If you set a Bounding Box or point filters, confirm they don't exclude all of your data

#### The form won't submit with multiple metrics
**Problem**: Submission is blocked with a message about the number of metric rows.

**Solutions**:
- When **Compares** is Category, Spatial Group, or Time, only one metric can be shown — remove extra metric rows
- To chart several metrics at once, set **Compares** back to `Metrics Only`

#### The Time comparison is rejected
**Problem**: The run fails when Compares is `Time`.

**Solutions**:
- Make sure the **Time Interval** is smaller than the comparison **Period** — e.g. use a `Week` interval to compare `Months`, or a `Month` interval to compare `Years`

#### Spatial Group comparison shows no series
**Problem**: With Compares set to Spatial Group, the chart is empty or unsplit.

**Solutions**:
- Enter the spatial feature group name exactly as it appears in EarthRanger (**Mapping → Spatial Feature Group Profiles**), including capitalization
- Confirm the group's regions actually overlap your patrol area — observations outside every region can't be assigned to a series

#### Encounter metrics show no values
**Problem**: Metrics like `Total Encounters` with an Aggregate Column show empty or zero bars.

**Solutions**:
- Confirm the event field you entered (e.g. `number_of_animals`) exists on the event types you're counting and holds numeric values
- Events without that field are skipped — check a few events in EarthRanger to confirm the field is filled in
- Without an Aggregate Column, `Total Encounters` simply counts events — use that if your events carry no numeric fields

#### Workflow runs very slowly
**Problem**: The run takes a long time to complete.

**Solutions**:
- Narrow the time range or restrict to specific patrol types
- The first run after installing a template can take longer while the workflow environment warms up — later runs are faster
