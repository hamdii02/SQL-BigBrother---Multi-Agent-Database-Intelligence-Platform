#!/usr/bin/env python3
"""
Script to create and populate the e-commerce database.
"""

import mysql.connector
from mysql.connector import Error
import os
from pathlib import Path

try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("⚠️  matplotlib not installed. Install with: pip install matplotlib")

def create_database():
    """Create the e-commerce database and load schema."""
    
    # Database configuration
    config = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': int(os.getenv('DB_PORT', '3306')),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
    }
    
    database_name = 'ecommerce_db'
    
    # Path to schema file
    schema_file = Path(__file__).parent / 'data' / '01_raw' / 'sample_schemas' / 'ecommerce.sql'
    
    if not schema_file.exists():
        print(f"❌ Schema file not found: {schema_file}")
        return False
    
    connection = None
    
    try:
        # Connect to MySQL server
        print(f"🔌 Connecting to MySQL server at {config['host']}:{config['port']}...")
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Drop database if exists (optional - comment out if you want to keep existing data)
            print(f"🗑️  Dropping existing database (if exists)...")
            cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")
            
            # Create database
            print(f"🏗️  Creating database: {database_name}...")
            cursor.execute(f"CREATE DATABASE {database_name}")
            
            # Use the database
            cursor.execute(f"USE {database_name}")
            
            # Read and execute schema file
            print(f"📄 Loading schema from: {schema_file.name}...")
            with open(schema_file, 'r') as f:
                schema_content = f.read()
            
            # Remove comments and split by semicolons
            lines = []
            for line in schema_content.split('\n'):
                line = line.strip()
                if line and not line.startswith('--'):
                    lines.append(line)
            
            clean_schema = ' '.join(lines)
            statements = [s.strip() for s in clean_schema.split(';') if s.strip()]
            
            print(f"   Found {len(statements)} SQL statements to execute")
            
            for i, statement in enumerate(statements, 1):
                try:
                    cursor.execute(statement)
                    # Extract table name for better feedback
                    if 'CREATE TABLE' in statement.upper():
                        table_name = statement.split('(')[0].replace('CREATE TABLE', '').strip()
                        print(f"   ✓ Created table: {table_name}")
                    else:
                        print(f"   ✓ Executed statement {i}/{len(statements)}")
                except Error as e:
                    print(f"   ❌ Error on statement {i}: {e}")
                    print(f"   Statement: {statement[:100]}...")
                    raise
            
            connection.commit()
            print("   ✓ All statements committed")
            
            # Verify tables were created
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            
            print(f"\n✅ Database created successfully!")
            print(f"📊 Created {len(tables)} tables:")
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table[0]}")
                count = cursor.fetchone()[0]
                print(f"   - {table[0]} ({count} rows)")
            
            # Insert sample data (optional)
            if input("\n📝 Do you want to add sample data? (y/n): ").lower() == 'y':
                insert_sample_data(cursor, connection)
            
            return True
            
    except Error as e:
        print(f"❌ MySQL Error: {e}")
        return False
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\n🔌 MySQL connection closed")


def insert_sample_data(cursor, connection):
    """Insert sample data into the database."""
    
    try:
        print("\n📝 Inserting sample data...")
        
        # Insert categories
        cursor.execute("""
            INSERT INTO categories (category_name, description) VALUES
            ('Electronics', 'Electronic devices and gadgets'),
            ('Clothing', 'Apparel and fashion items'),
            ('Books', 'Books and literature'),
            ('Home & Garden', 'Home improvement and garden supplies'),
            ('Sports', 'Sports equipment and accessories')
        """)
        print("   ✓ Added 5 categories")
        
        # Insert customers
        cursor.execute("""
            INSERT INTO customers (first_name, last_name, email, phone, city, state, country) VALUES
            ('John', 'Doe', 'john.doe@example.com', '555-0101', 'New York', 'NY', 'USA'),
            ('Jane', 'Smith', 'jane.smith@example.com', '555-0102', 'Los Angeles', 'CA', 'USA'),
            ('Bob', 'Johnson', 'bob.johnson@example.com', '555-0103', 'Chicago', 'IL', 'USA'),
            ('Alice', 'Williams', 'alice.williams@example.com', '555-0104', 'Houston', 'TX', 'USA'),
            ('Charlie', 'Brown', 'charlie.brown@example.com', '555-0105', 'Phoenix', 'AZ', 'USA')
        """)
        print("   ✓ Added 5 customers")
        
        # Insert products
        cursor.execute("""
            INSERT INTO products (product_name, description, category_id, price, cost, stock_quantity, sku) VALUES
            ('Laptop Pro 15', 'High-performance laptop', 1, 1299.99, 800.00, 50, 'LAPTOP-001'),
            ('Wireless Mouse', 'Ergonomic wireless mouse', 1, 29.99, 15.00, 200, 'MOUSE-001'),
            ('Cotton T-Shirt', 'Comfortable cotton t-shirt', 2, 19.99, 8.00, 500, 'SHIRT-001'),
            ('Running Shoes', 'Professional running shoes', 5, 89.99, 45.00, 150, 'SHOES-001'),
            ('Python Programming Book', 'Learn Python from scratch', 3, 39.99, 20.00, 100, 'BOOK-001'),
            ('Smart Watch', 'Fitness tracking smart watch', 1, 299.99, 180.00, 75, 'WATCH-001'),
            ('Yoga Mat', 'Non-slip yoga mat', 5, 24.99, 12.00, 300, 'YOGA-001'),
            ('Coffee Maker', 'Automatic coffee maker', 4, 79.99, 40.00, 80, 'COFFEE-001')
        """)
        print("   ✓ Added 8 products")
        
        # Insert orders
        cursor.execute("""
            INSERT INTO orders (customer_id, status, total_amount, payment_method, payment_status) VALUES
            (1, 'completed', 1329.98, 'credit_card', 'paid'),
            (2, 'processing', 49.98, 'paypal', 'paid'),
            (3, 'pending', 89.99, 'credit_card', 'pending'),
            (4, 'completed', 339.98, 'credit_card', 'paid')
        """)
        print("   ✓ Added 4 orders")
        
        # Insert order items
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal) VALUES
            (1, 1, 1, 1299.99, 1299.99),
            (1, 2, 1, 29.99, 29.99),
            (2, 3, 2, 19.99, 39.98),
            (2, 7, 1, 24.99, 24.99),
            (3, 4, 1, 89.99, 89.99),
            (4, 6, 1, 299.99, 299.99),
            (4, 8, 1, 79.99, 79.99)
        """)
        print("   ✓ Added 7 order items")
        
        # Insert reviews
        cursor.execute("""
            INSERT INTO reviews (product_id, customer_id, rating, title, comment, is_verified_purchase) VALUES
            (1, 1, 5, 'Excellent laptop!', 'Best purchase ever. Fast and reliable.', TRUE),
            (4, 3, 4, 'Great shoes', 'Comfortable for long runs.', TRUE),
            (6, 4, 5, 'Amazing watch', 'Perfect for fitness tracking.', TRUE)
        """)
        print("   ✓ Added 3 reviews")
        
        # Insert shipping methods
        cursor.execute("""
            INSERT INTO shipping_methods (method_name, description, base_cost, estimated_days) VALUES
            ('Standard', 'Standard shipping', 5.99, 7),
            ('Express', 'Express shipping', 15.99, 3),
            ('Overnight', 'Next day delivery', 29.99, 1),
            ('Free Shipping', 'Free standard shipping on orders over $50', 0.00, 10)
        """)
        print("   ✓ Added 4 shipping methods")
        
        connection.commit()
        print("\n✅ Sample data inserted successfully!")
        
        # Plot the database schema
        plot_database_schema(cursor)
        
    except Error as e:
        print(f"❌ Error inserting sample data: {e}")
        connection.rollback()


def plot_database_schema(cursor):
    """Create a visual representation of the database schema."""
    
    if not HAS_MATPLOTLIB:
        print("\n📊 Skipping database visualization (matplotlib not installed)")
        return
    
    try:
        print("\n📊 Generating database schema visualization...")
        
        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        
        # Get column information for each table
        table_info = {}
        foreign_keys = []
        
        for table in tables:
            cursor.execute(f"DESCRIBE {table}")
            columns = cursor.fetchall()
            table_info[table] = columns
            
            # Get foreign key relationships
            cursor.execute(f"""
                SELECT 
                    COLUMN_NAME,
                    REFERENCED_TABLE_NAME,
                    REFERENCED_COLUMN_NAME
                FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                WHERE TABLE_SCHEMA = DATABASE()
                AND TABLE_NAME = '{table}'
                AND REFERENCED_TABLE_NAME IS NOT NULL
            """)
            fks = cursor.fetchall()
            for fk in fks:
                foreign_keys.append((table, fk[1]))  # (from_table, to_table)
        
        # Create figure
        fig, ax = plt.subplots(figsize=(16, 12))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Calculate positions for tables (grid layout)
        num_tables = len(tables)
        cols = 4
        rows = (num_tables + cols - 1) // cols
        
        table_positions = {}
        table_width = 2.0
        table_height_base = 0.3
        
        for idx, table in enumerate(tables):
            row = idx // cols
            col = idx % cols
            x = col * 2.5 + 0.5
            y = 9 - (row * 2.5)
            
            # Calculate height based on number of columns
            num_cols = len(table_info[table])
            table_height = table_height_base + (num_cols * 0.15)
            
            table_positions[table] = (x, y, table_width, table_height)
            
            # Draw table box
            box = FancyBboxPatch(
                (x, y - table_height), table_width, table_height,
                boxstyle="round,pad=0.05",
                edgecolor='#2196F3',
                facecolor='#E3F2FD',
                linewidth=2
            )
            ax.add_patch(box)
            
            # Draw table name header
            header = FancyBboxPatch(
                (x, y - 0.25), table_width, 0.25,
                boxstyle="round,pad=0.02",
                edgecolor='#1976D2',
                facecolor='#2196F3',
                linewidth=1
            )
            ax.add_patch(header)
            
            # Add table name
            ax.text(
                x + table_width/2, y - 0.125,
                table.upper(),
                ha='center', va='center',
                fontsize=9, fontweight='bold',
                color='white'
            )
            
            # Add column names
            y_offset = 0.4
            for col_name, col_type, *rest in table_info[table][:8]:  # Limit to 8 columns
                col_text = f"{col_name}: {col_type.decode() if isinstance(col_type, bytes) else col_type}"
                if len(col_text) > 35:
                    col_text = col_text[:32] + "..."
                ax.text(
                    x + 0.1, y - y_offset,
                    col_text,
                    fontsize=7,
                    va='top'
                )
                y_offset += 0.15
            
            if len(table_info[table]) > 8:
                ax.text(
                    x + 0.1, y - y_offset,
                    f"... +{len(table_info[table]) - 8} more",
                    fontsize=7,
                    va='top',
                    style='italic',
                    color='gray'
                )
        
        # Draw foreign key relationships
        for from_table, to_table in foreign_keys:
            if from_table in table_positions and to_table in table_positions:
                from_x, from_y, from_w, from_h = table_positions[from_table]
                to_x, to_y, to_w, to_h = table_positions[to_table]
                
                # Calculate connection points
                from_center_x = from_x + from_w / 2
                from_center_y = from_y - from_h / 2
                to_center_x = to_x + to_w / 2
                to_center_y = to_y - to_h / 2
                
                # Draw arrow
                ax.annotate(
                    '',
                    xy=(to_center_x, to_center_y),
                    xytext=(from_center_x, from_center_y),
                    arrowprops=dict(
                        arrowstyle='->',
                        color='#FF9800',
                        lw=1.5,
                        alpha=0.6,
                        connectionstyle="arc3,rad=0.3"
                    )
                )
        
        # Add title
        plt.title(
            'E-commerce Database Schema',
            fontsize=18,
            fontweight='bold',
            pad=20,
            color='#1976D2'
        )
        
        # Add legend
        legend_elements = [
            mpatches.Patch(facecolor='#E3F2FD', edgecolor='#2196F3', label='Table'),
            mpatches.Patch(facecolor='none', edgecolor='#FF9800', label='Foreign Key')
        ]
        ax.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        # Add footer
        ax.text(
            5, 0.2,
            f'Total Tables: {len(tables)} | Total Relationships: {len(foreign_keys)}',
            ha='center',
            fontsize=10,
            style='italic',
            color='gray'
        )
        
        plt.tight_layout()
        
        # Save the figure
        output_file = Path(__file__).parent / 'ecommerce_db_schema.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"   ✓ Schema diagram saved to: {output_file.name}")
        
        # Show the plot
        plt.show()
        
    except Exception as e:
        print(f"   ⚠️  Could not generate visualization: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("🛒 E-commerce Database Setup Script")
    print("=" * 60)
    print()
    
    # Check if MySQL connection details are correct
    db_user = os.getenv('DB_USER', 'root')
    db_host = os.getenv('DB_HOST', 'localhost')
    
    print(f"📋 Configuration:")
    print(f"   Host: {db_host}")
    print(f"   User: {db_user}")
    print()
    
    proceed = input("⚠️  This will DROP and recreate the 'ecommerce_db' database. Continue? (y/n): ")
    
    if proceed.lower() == 'y':
        success = create_database()
        if success:
            print("\n" + "=" * 60)
            print("🎉 Setup completed successfully!")
            print("=" * 60)
            print("\nYou can now:")
            print("  1. Start the SQL BigBrother server")
            print("  2. Upload the schema through the frontend")
            print("  3. Start asking questions about your database!")
        else:
            print("\n❌ Setup failed. Please check the error messages above.")
    else:
        print("\n❌ Setup cancelled by user")
