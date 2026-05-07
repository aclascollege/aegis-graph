import asyncio
import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich import box

# Set working directory to project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from main_pipeline import AegisGraphEngine

console = Console()

async def run_professional_demo():
    """
    Official ACLAS College Aegis-Graph Demonstration Script.
    """
    engine = AegisGraphEngine()
    
    console.print(Panel.fit(
        "[bold green]AEGIS-GRAPH[/bold green] // [bold white]SOVEREIGN AUDIT NETWORK[/bold white] // [bold cyan]OFFICIAL DEMO v1.2[/bold cyan]\n"
        "[dim]Sovereign Node: SOV_ATL_0782 | Kernel: MCP-Native | Auth: ACLAS Authority[/dim]",
        border_style="green",
        box=box.DOUBLE
    ))

    scenarios = [
        {"name": "Atlanta College (ACLAS) Alumni", "file": "aclas_alumni_2025.png", "type": "Institutional"},
        {"name": "Suspect Diploma Factory", "file": "fake_degree_sample.png", "type": "Unrecognized"},
        {"name": "Graham Int. University", "file": "graham_university_transcript.pdf", "type": "Blacklisted"}
    ]

    for scenario in scenarios:
        console.print(f"\n[bold yellow]>>> AUDIT TASK:[/bold yellow] {scenario['name']} ([dim]{scenario['file']}[/dim])")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=40),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task1 = progress.add_task("[cyan]Vision Forensics...", total=100)
            task2 = progress.add_task("[magenta]Graph Navigation...", total=100)
            task3 = progress.add_task("[blue]Logic Audit...", total=100)

            while not progress.finished:
                await asyncio.sleep(0.01)
                progress.update(task1, advance=0.8)
                if progress.tasks[0].completed > 50:
                    progress.update(task2, advance=0.6)
                if progress.tasks[1].completed > 50:
                    progress.update(task3, advance=0.5)

        # Execute real audit
        result = await engine.execute_audit(scenario['file'])
        
        # Display Result Table
        verdict = result['verdict']
        risk_score = result['risk_score']
        if verdict.startswith("REJECTED"):
            node_status = "[red]BLOCKED[/red]"
        elif verdict == "NEEDS_REVIEW":
            node_status = "[yellow]REVIEW[/yellow]"
        else:
            node_status = "[green]SYNCED[/green]"

        if risk_score >= 85:
            risk_status = "[red]HIGH[/red]"
        elif risk_score >= 40:
            risk_status = "[yellow]MODERATE[/yellow]"
        else:
            risk_status = "[green]LOW[/green]"

        # Display Result Table
        table = Table(title=f"Audit Resolution: {scenario['name']}", box=box.ROUNDED, border_style="cyan")
        table.add_column("Layer", style="dim")
        table.add_column("Metric", style="bold")
        table.add_column("Status", justify="right")

        table.add_row("Institutional Node", verdict, node_status)
        table.add_row("Risk Score", f"{risk_score:.1f}/100", risk_status)
        table.add_row("MCP Trace ID", result['trace_id'][:12], "[dim]ENCRYPTED[/dim]")

        console.print(table)
        console.print(f"[dim]Reasoning Trail: {' -> '.join(result['reasoning'][:3])}...[/dim]\n")

    console.print(Panel(
        "[bold green]DEMO COMPLETE[/bold green]\n"
        "[white]Demo complete. Production deployments must anchor server-signed audit trails before issuing verification certificates.[/white]",
        border_style="white",
        box=box.SQUARE,
        padding=(1, 2)
    ))


if __name__ == "__main__":
    try:
        asyncio.run(run_professional_demo())
    except KeyboardInterrupt:
        console.print("\n[bold red]Demo interrupted by user.[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red][ERROR] Error during demo execution:[/bold red] {e}")
