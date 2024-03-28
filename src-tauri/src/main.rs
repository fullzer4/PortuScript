#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn lsp(text: &str) -> String {
    format!("Text received: {}", text)
}

#[tauri::command]
fn interpreter(file: &str) -> String {
    format!("File received: {}", file)
}

#[tauri::command]
fn memory_view(file: &str) -> String {
    format!("Memory address: {}", file)
}

#[tauri::command]
fn linter(file: &str) -> String {
    format!("linter")
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
