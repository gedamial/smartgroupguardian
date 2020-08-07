# Current features

Here you can find the full features list, from the just proposed ones to the working ones.
Clicking on the feature you'll be redirect to its documentation section. **If the documentation is not available for the specific feature, you'll be redirect to a default error page.**

## List of commands

Available statuses:

- ***Active*** - The feature is developed and available
- ***Failing*** - The feature is developed, but not available due to errors or maintenance
- ***Developing*** - The feature is being developed
- ***Proposed*** - The feature has just been proposed (referring to the GitHub username or the Pull Request where the feature has been requested)

## Members management

| Status | Command Name | Description |
| :-:       | :-:             | -           |
| ***Developing*** | ```warn``` | Warns a member |
| ***Active*** | ```kick``` | Kicks a member out of the group |
| ***Active*** | ```ban``` | Removes permanently a member, disallowing them to re-join the group. |
|***Active***| ```unban``` | Removes a user from the banned users list |
|***Active***| ```mute``` | Mutes a member |
|***Active***| ```unmute``` | Unmutes a member |
|***Active***| ```ping``` | Checks whether the bot is up and running |

## Features

| Status    | Feature  | Description |
| :-:       | :-:             | -           |
| ***Developing*** | Welcome Message | Sends a welcome message as soon as a member joins the group |
| ***Developing*** | Night Mode | Members are not allowed to send messages from a given time for a given number of hours |
| ***Developing*** | Captcha | Any new member needs to press a button to make sure they're not a robot |
| ***Active*** | Garbage Collector | Automatically deletes any memeber's unsuccessful attempt to call an admin-only command for the bot |
| ***Active*** | Report to admin | By using @admin, any member can alert all the admins of the group |
| ***Developing*** | Bad Words detector | Automatically recognizes bad words and warns the member who wrote them |