#0x19. Postmortem using 0x0E. Web stack debugging #1

Issue Summary
Duration of the outage: The outage lasted for 1hour rom 9AM TO 10AM East African Time.
Impact: During the outage, the server experienced high CPU usage, resulting in slow
response times timeouts. Approximately 70% of users were affected, leading to a degraded
user experience and a noticeable drop in site performance.
Root cause: The root cause was an infinite loop in the server's application code, which
caused the server process to consume excessive CPU resources.

Timeline
> 9:00 AM: The issue was detected by automated monitoring tools, which triggered an alert
due to the server's CPU usage exceeding 90%.
> 9:05 AM: The on-call engineer received the alert anf began investigating the servers performance
metrics.
> 9:10 AM: Initial assumptions were made that a sudden traffic spike might be causing the high
CPU usage, leading the engineer to check the server logs for unusual activity.
> 9:20 AM: The engineer noticed that the CPU usage was tied to a specific process related
to the web application.
> 9:25 AM: Further investigation revealed that the issue was not due to external factors,
but rather an internal problem with the application code.
> 9:30 AM: The engineer reviewed the latest code changes and identified a recently deployed
update that introduced an infinite loop.
> 9:40 AM: The application was rolled back to the previous stable version to halt an infinite loop.
> 9:50 AM: The server's CPU usage began to stabilize, and the response times improved.
> 10:00 AM: The website's performance returned to normal, and the incident was was officially resolved.

Root cause and Resolution
Root cause: The infinite loop was introduced in the server's code during a recent deployment. The loop
caused the server to continuously execute the same code block without termination, leading to excessive
CPU usage and degraded performance.
Resolution: The resolution involved rolling back the recent deployment to a stable version of the application
cod, which removed the infinite loop and restored normal server operations.

Corrective and Preventative Measures
Improvements:
Enhance code review processes to catch logical errors like infinite loops before deployment.
Implement automated tests that simulate high-load scenarios to identify performance issues in development.
Increase monitoring granularity to detect CPU usage spikes tied to specific processes more quickly.
Task List:
Conduct a postmortem review with the development team to discuss the introduction of the infinite loop and how it was missed during code review.
Update the code review checklist to include checks for potential infinite loops and other performance risks.
Implement additional automated testing focused on performance and load handling in the CI/CD pipeline.
Schedule training for developers on common pitfalls like infinite loops and best practices for preventing them.
