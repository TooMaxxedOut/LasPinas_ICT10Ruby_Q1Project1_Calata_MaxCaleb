from pyscript import display, document

def generateSKU():
    document.getElementById("sku_output").innerHTML = ""


    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    if category == "evil":
        display("no.", target="sku_output")
    elif category == "default":
        display("Choose a Product Category first, then click the button after.", target="sku_output")
    else:
        sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
        display("SKU: " + sku, target="sku_output")

def print():
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")
    prod9 = document.getElementById("item9")
    prod10 = document.getElementById("item10")


    subtotal = (
        float(prod1.value) * prod1.checked
        + float(prod2.value) * prod2.checked
        + float(prod3.value) * prod3.checked
        + float(prod4.value) * prod4.checked
        + float(prod5.value) * prod5.checked
        + float(prod6.value) * prod6.checked
        + float(prod7.value) * prod7.checked
        + float(prod8.value) * prod8.checked
        + float(prod9.value) * prod9.checked
        + float(prod10.value) * prod10.checked
    )

    tax_rate = 0.12
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""
    <h2>     RECEIPT     </h2>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT: ₱{tax:.2f}</p>
    <h3>Total: ₱{total:.2f}</h3>
    """

    document.getElementById("print").innerHTML = receipt
