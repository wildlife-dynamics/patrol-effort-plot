# Patrol Effort Plot Workflow

## Introduction

This workflow helps you to track how your patrol effort and patrol results change over time. It turns **EarthRanger** patrol data into a single interactive chart of the patrol metrics you choose — as bars or lines, summarized by week, month, or any other time interval.

**What this workflow does:**
- Downloads patrols and the events reported during those patrols from **EarthRanger**
- Calculates patrol metrics such as patrol count, patrol days, distance covered, time on patrol, event counts, and encounter rates
- Reads each patrol's legs — the segments an **EarthRanger** patrol is made of — for active and elapsed duration, leg counts and member-days, and for who ran the patrol (team, members, assets)
- Summarizes each metric over a time interval you choose (year, month, week, day, or hour)
- Optionally splits a metric into separate series by category (e.g. event type, patrol team or member), by spatial region, or across time periods (e.g. compare this month against last month)
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
   - To group or compare by **Team**, **Member** or **Asset**, your EarthRanger site must record the patrol roster on each patrol leg (the patrol leg schema). On a site without it, those options show a single `None` group and **Member-days** draws no bars; every other metric still works

## Installation

1. Select "Workflow Templates" tab
2. Click "+ Add Template"
3. Copy and paste this URL https://github.com/wildlife-dynamics/patrol-effort-plot and wait for the workflow template to be downloaded and initialized
4. The template will now appear in your available template list

## Configuration Guide

### Basic Configuration

#### 1. Workflow Details
Give your workflow run a recognizable identity.

- **Workflow Name** (required): A name for this analysis
  - Example: `Patrol Effort Plot`
- **Workflow Description** (optional): A short note on what this run covers
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
- **Patrol Status** and **Event State** sit under Advanced Configurations — see below.

#### 5. Filter Data
Optionally restrict the data by location or movement characteristics. All settings here sit under Advanced Configurations — see below; most users can leave them at their defaults.

#### 6. Group Data
Optionally split the results into separate dashboard views — one chart per group.

Add one or more grouping rows (optional). Leave the list empty to produce a single chart for the whole time range.

- **Category**: Split by a patrol attribute — **Index Name**:
  - Options: `Patrol Serial Number`, `Patrol Type`, `Patrol Subject`, `Team`, `Member`, `Asset`
  - `Team`, `Member` and `Asset` come from the patrol legs recorded in EarthRanger. `Member` and `Asset` give one chart per ranger or vehicle, and a leg shared by several members counts fully for each of them. On a site without the patrol leg roster these three produce a single `None` view.
- **Time**: Split by time period — **Time**
  - Options: `Year (example: 2024)`, `Month (example: September)`, `Year and Month (example: 2023-01)`, `Day of the year as a number (example: 365)`, `Day of the month as a number (example: 31)`, `Day of the week (example: Sunday)`, `Hour (24-hour clock) as number (example: 22)`, `Date (example: 2025-01-31)`
- **Spatial**: Split by the regions of an EarthRanger spatial feature group — **Spatial Regions**: the group's name (**Mapping → Spatial Feature Group Profiles**)

#### 7. Trend Chart
The heart of the workflow: pick the metrics, the time interval, and what each series represents.

- **Metrics** (required): Add one or more metric rows. Each metric becomes one series on the chart (default: `Patrol Count`). Available metrics:
  - **Patrol Count**: Number of patrols
  - **Patrol Days**: Number of distinct days with patrol movement
  - **Total Distance** / **Total Duration**: Distance covered / time spent on patrol — pick the **Unit** (`Kilometers (km)` or `Meters (m)`; `Hours (h)` or `Days (d)`)
  - **Active Duration**: Time the patrol legs were active, excluding pauses — **Unit** `Hours (h)` (default) or `Days (d)`
  - **Elapsed Duration**: Time from each patrol's first leg start to its last leg end, pauses included — **Unit** `Hours (h)` (default) or `Days (d)`
  - **Leg Count**: Number of patrol legs
  - **Member-days**: Members on each leg times the days it spans, summed. Draws no bars on a site without the patrol leg roster
  - **Total Events**: Number of events reported during patrols
  - **Total Encounters**: Sum of a numeric event field (set **Event Field to Sum** to the event field, e.g. `number_of_animals`); leave it empty to count events
  - **Encounters per Distance** / **Encounters per Duration** / **Encounters per Patrol** / **Encounters per Patrol Day**: Encounter rates relative to patrol effort — the same **Event Field to Sum** choice, plus a **Unit** for the distance and duration rates
  - **Area Covered (Merged)** / **Area Covered (Unmerged)**: Area swept by patrols given a **Swath Width (m)** (default: `500`)
  - **Custom**: Your own **Statistic** (`sum`, `count`, `min`, `max`, `mean`, `nunique`, `median`) over any data **Column**, shown under your **Display Name** with **Decimal Places** (default: `2`); tick **Convert Units** to convert the result between units
- **Time Interval** (required): The time bucket for the x-axis — how metrics are summarized over time
  - Default: `Week`
  - Options: Year, Month, Week, Day, Hour
- **Compares** (required): What each series represents
  - Default: `Metrics Only`
  - **Metrics Only**: One series per metric row
  - **Category**: The single metric split into one series per category value — choose the **Category**: `Event Type` (default), `Patrol Type`, `Patrol Subject`, `Patrol Serial Number`, `Team`, `Member` or `Asset`. `Member` and `Asset` give one series per ranger or vehicle, each credited with the full leg; on a site without the patrol leg roster they give a single `None` series
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

### Advanced Configuration

These optional settings provide additional control over your workflow. In the app they sit under
the "Advanced Configurations" accordion of their card.

#### Patrol and event filters (Patrol and Event Types)
Which patrols and events are fetched.

- **Patrol Status**: Which patrol statuses to include
  - Default: `Done`
  - Options: Active, Overdue, Done, Cancelled
- **Event State**: Which event states to count; leave empty for all
  - Options: New, Active, Resolved, Review

#### Location and track filters (Filter Data)
Restrict the data by location or movement characteristics.

- **Bounding Box**: Only include patrol observations and events inside this rectangle (west/south/east/north coordinates)
- **Filter Exact Point Coordinates**: Exclude observations recorded at these exact coordinates (e.g. known default GPS points)
- **Trajectory Filter**: Limits on segment speed, duration, and distance used when building patrol tracks — useful for removing GPS noise

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

Note: encounter-rate metrics are labeled automatically — e.g. `Events per Patrol Day`, or `Number Of Animals per km` when an Event Field to Sum is set.

### How the Results Are Calculated

#### Patrol effort from tracks
**Patrol Count** counts distinct patrols with tracked movement in each time bucket, and **Patrol Days** counts the distinct calendar days on which patrol movement was recorded. **Total Distance** and **Total Duration** add up the tracked segments between consecutive GPS fixes, after the **Trajectory Filter** has removed implausible segments. **Area Covered** buffers each tracked segment by half the **Swath Width (m)** on each side: *Merged* takes the union of those buffers, so overlapping passes count once; *Unmerged* adds them up, so repeat coverage counts again.

#### Encounter rates
**Total Encounters** and the four rate metrics count the patrol events in each bucket, or sum the **Event Field to Sum** over them (events without that field are skipped). Each rate divides that figure by the matching effort in the same bucket: distance covered, time on patrol, number of patrols, or patrol days.

#### Patrol legs
An EarthRanger patrol is made of one or more legs, each with its own start, end, team, members and assets. **Active Duration** adds up the legs themselves, so pauses are excluded; **Elapsed Duration** measures each patrol from its first leg's start to its last leg's end, pauses included. **Leg Count** counts legs. **Member-days** multiplies the members on a leg by the days it spans and adds the results. A leg is placed in the time bucket of its start.

When **Compares** is `Spatial Group` or a **Spatial** grouper is set, a leg's durations and member-days are shared between regions in proportion to the length of its track in each, and the leg counts once in every region it touches. On a site that does not record the leg roster the tracks cannot be matched to their legs, so leg metrics are left out of spatial views and **Team**, **Member** and **Asset** show `None`. Grouping or comparing by **Member** or **Asset** credits each ranger or vehicle with the whole leg, except **Member-days**, which is divided among the members.

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
  - Metrics: `Total Encounters` with Event Field to Sum `number_of_animals`, and `Encounters per Distance` with unit `km` and the same Event Field to Sum
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
- Check the **Patrol Status** filter: by default only `Done` patrols are included
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

#### Team, Member or Asset shows only `None`
**Problem**: Grouping or comparing by **Team**, **Member** or **Asset** gives a single `None` view or series.

**Solutions**:
- Your EarthRanger site does not record the roster on patrol legs (the patrol leg schema). Ask your EarthRanger administrator whether it can be enabled; until then group by `Patrol Subject` instead
- Confirm the patrols in your time range have a team, members or assets filled in on their legs

#### Member-days draws no bars
**Problem**: The `Member-days` series is empty while the other leg metrics show values.

**Solutions**:
- Member-days needs the member list on each leg; on a site without the patrol leg roster it has nothing to count — use `Active Duration` or `Leg Count` instead
- Check that the legs in your time range list their members in EarthRanger

#### Encounter metrics show no values
**Problem**: Metrics like `Total Encounters` with an Event Field to Sum show empty or zero bars.

**Solutions**:
- Confirm the event field you entered (e.g. `number_of_animals`) exists on the event types you're counting and holds numeric values
- Events without that field are skipped — check a few events in EarthRanger to confirm the field is filled in
- Without an Event Field to Sum, `Total Encounters` simply counts events — use that if your events carry no numeric fields

#### Workflow runs very slowly
**Problem**: The run takes a long time to complete.

**Solutions**:
- Narrow the time range or restrict to specific patrol types
- The first run after installing a template can take longer while the workflow environment warms up — later runs are faster
