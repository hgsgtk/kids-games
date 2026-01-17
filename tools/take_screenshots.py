#!/usr/bin/env python3
"""
Screenshot Automation Tool for Kids Games Collection

Usage:
    python tools/take_screenshots.py [options]

Options:
    --all                Take screenshots of all games
    --game FILENAME      Take screenshot of a specific game (e.g., abc-bouncing-balls.html)
    --config FILE        Use custom config file (default: tools/screenshot_config.json)
    --port PORT          Server port (default: 8000)
    --output DIR         Output directory (default: screenshots)
    --width WIDTH        Viewport width (default: 1200)
    --height HEIGHT      Viewport height (default: 800)

Examples:
    # Take screenshots of all games
    python tools/take_screenshots.py --all

    # Take screenshot of a specific game
    python tools/take_screenshots.py --game abc-bouncing-balls.html

    # Use custom port and output directory
    python tools/take_screenshots.py --all --port 3000 --output img/screenshots
"""

import asyncio
import argparse
import json
import os
import sys
from pathlib import Path
from playwright.async_api import async_playwright


def load_config(config_path: str) -> dict:
    """Load configuration from JSON file"""
    if not os.path.exists(config_path):
        print(f"⚠️  Config file not found: {config_path}")
        print("Using default configuration...")
        return {"games": []}
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_default_config() -> dict:
    """Get default configuration"""
    return {
        "games": [
            {
                "file": "abc-bouncing-balls.html",
                "wait_time": 3,
                "description": "ABC Song with Bouncing Balls"
            },
            {
                "file": "4d-baby-animation.html",
                "wait_time": 2,
                "description": "Baby's 4D Wonder World"
            },
            {
                "file": "alphabet-typing.html",
                "wait_time": 2,
                "description": "Alphabet Typing A→Z"
            },
            {
                "file": "number-typing.html",
                "wait_time": 2,
                "description": "Number Typing Game"
            },
            {
                "file": "3d-number-typing.html",
                "wait_time": 3,
                "description": "3D Number Typing Adventure"
            },
            {
                "file": "4d-number-rush.html",
                "wait_time": 3,
                "description": "4D Number Journey"
            },
            {
                "file": "baby-countdown-timer.html",
                "wait_time": 2,
                "description": "Baby Countdown Timer"
            },
            {
                "file": "elevator-game.html",
                "wait_time": 3,
                "description": "Elevator Game"
            },
            {
                "file": "mochitsuki-game.html",
                "wait_time": 2,
                "description": "Mochitsuki Game"
            },
            {
                "file": "tako-age-game.html",
                "wait_time": 3,
                "description": "Tako-age Game"
            },
            {
                "file": "clock-countdown-game.html",
                "wait_time": 2,
                "description": "Clock Countdown Game"
            },
            {
                "file": "animal-catch-game.html",
                "wait_time": 2,
                "description": "Animal Catch Game"
            }
        ]
    }


async def take_screenshot(page, game: dict, base_url: str, output_dir: str):
    """Take a screenshot of a game"""
    filename = game['file']
    wait_time = game.get('wait_time', 2)
    description = game.get('description', filename)
    
    # Generate output filename
    output_filename = Path(filename).stem + '.png'
    output_path = os.path.join(output_dir, output_filename)
    
    url = f"{base_url}/{filename}"
    print(f"📸 Taking screenshot: {description}")
    print(f"   URL: {url}")
    
    try:
        # Navigate to the game
        await page.goto(url, wait_until='networkidle', timeout=30000)
        
        # Wait for the specified time to let animations start
        await asyncio.sleep(wait_time)
        
        # Take screenshot
        await page.screenshot(path=output_path, full_page=False)
        print(f"   ✓ Saved: {output_path}\n")
        return True
        
    except Exception as e:
        print(f"   ✗ Error: {e}\n")
        return False


async def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Take screenshots of kids games',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--all', action='store_true', help='Take screenshots of all games')
    parser.add_argument('--game', type=str, help='Take screenshot of a specific game file')
    parser.add_argument('--config', type=str, default='tools/screenshot_config.json',
                       help='Config file path (default: tools/screenshot_config.json)')
    parser.add_argument('--port', type=int, default=8000, help='Server port (default: 8000)')
    parser.add_argument('--output', type=str, default='screenshots',
                       help='Output directory (default: screenshots)')
    parser.add_argument('--width', type=int, default=1200, help='Viewport width (default: 1200)')
    parser.add_argument('--height', type=int, default=800, help='Viewport height (default: 800)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.all and not args.game:
        parser.print_help()
        print("\n⚠️  Error: Please specify --all or --game")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Load configuration
    if os.path.exists(args.config):
        config = load_config(args.config)
    else:
        print(f"⚠️  Config file not found: {args.config}")
        print("Creating default configuration...")
        config = get_default_config()
        # Save default config
        os.makedirs(os.path.dirname(args.config), exist_ok=True)
        with open(args.config, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✓ Created config file: {args.config}\n")
    
    # Filter games if specific game requested
    games_to_process = config['games']
    if args.game:
        games_to_process = [g for g in games_to_process if g['file'] == args.game]
        if not games_to_process:
            print(f"⚠️  Game not found in config: {args.game}")
            sys.exit(1)
    
    # Base URL
    base_url = f"http://localhost:{args.port}"
    
    print(f"🎮 Kids Games Screenshot Tool")
    print(f"=" * 50)
    print(f"Server: {base_url}")
    print(f"Output: {args.output}")
    print(f"Viewport: {args.width}x{args.height}")
    print(f"Games to process: {len(games_to_process)}")
    print(f"=" * 50)
    print()
    
    # Take screenshots
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        
        # Create a new page with specified viewport
        page = await browser.new_page(viewport={'width': args.width, 'height': args.height})
        
        # Take screenshots
        success_count = 0
        for game in games_to_process:
            if await take_screenshot(page, game, base_url, args.output):
                success_count += 1
            # Small delay between screenshots
            await asyncio.sleep(0.5)
        
        # Close browser
        await browser.close()
    
    # Summary
    print(f"=" * 50)
    print(f"✓ Completed: {success_count}/{len(games_to_process)} screenshots")
    print(f"=" * 50)
    
    if success_count < len(games_to_process):
        sys.exit(1)


if __name__ == '__main__':
    asyncio.run(main())
