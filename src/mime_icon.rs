use cosmic::widget::icon;
use std::path::Path;

pub const FALLBACK_MIME_ICON: &str = "text-x-generic";

pub fn mime_for_path(path: &Path) -> String {
    mime_guess::from_path(path)
        .first()
        .map(|m| m.to_string())
        .unwrap_or_else(|| "application/octet-stream".to_string())
}

pub fn mime_icon(mime: &str, size: u16) -> icon::Handle {
    let icon_name = mime_to_icon_name(mime);
    icon::from_name(icon_name).size(size).handle()
}

fn mime_to_icon_name(mime: &str) -> &'static str {
    match mime {
        "application/pdf" => "application-pdf",
        "application/zip"
        | "application/gzip"
        | "application/x-tar"
        | "application/x-compressed-tar"
        | "application/x-bzip2"
        | "application/x-xz"
        | "application/zstd" => "package-x-generic",
        "application/json" => "text-x-generic",
        "application/xml" | "application/xhtml+xml" => "text-html",
        "application/javascript" | "application/x-javascript" => "text-x-script",
        "application/x-shellscript" => "text-x-script",
        "application/x-executable" | "application/x-sharedlib" => "application-x-executable",
        _ => {
            let type_ = mime.split('/').next().unwrap_or("application");
            match type_ {
                "text" => "text-x-generic",
                "image" => "image-x-generic",
                "audio" => "audio-x-generic",
                "video" => "video-x-generic",
                "font" => "font-x-generic",
                _ => FALLBACK_MIME_ICON,
            }
        }
    }
}
