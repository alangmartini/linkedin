let list_jobs = document.querySelector("#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__list > div > ul")

let job_data = document.querySelector("#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div")

// Search for the button with inner text easy apply
let buttons = job_data.querySelectorAll("button")
buttons.forEach(button => {
  if (button.innerText.toLowerCase().includes("easy apply")) {
    console.log("Easy apply button found", button)
  }
})

// Get the element by the property labelledby that is
// equal to jobs-apply-header
let apply_header = document.querySelector("[aria-labelledby='jobs-apply-header']")
// Get all inputs in the page
apply_header.querySelectorAll("input")

// Get all selects
apply_header.querySelectorAll("select")